import glob
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='template')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/scrap/{keyword}", response_class=HTMLResponse)
async def 수집하기(request: Request, keyword:str):
    day_str = datetime.today().strftime('%Y-%m-%d')
    title = []
    url = f'https://www.google.com/search?q={keyword}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.62 Safari/537.36'}
    for i in range(0, 99, 10):
        res = requests.get(url + f"&start={i}&", headers=headers)
        bsObject = BeautifulSoup(res.text, "html.parser")
        text = bsObject.find_all("h3", {"class": "LC20lb MBeuO DKV0Md"})
        print(i, "개 수집완료")
        for j in text:
            title.append(j.text)
    df = pd.DataFrame({'keyword':keyword, 'title': title, 'date': day_str})
    print("수집완료"), df.to_csv(f'./{keyword}.csv', index=False)
    return templates.TemplateResponse("done.html", {"request": request, "keyword": keyword})
    # return db

@app.get("/rename/{keyword}/{rename}", response_class=HTMLResponse)
async def 다른이름으로저장(request: Request, keyword: str, rename: str):
    try:
        list_csv = glob.glob(f'./{keyword}*.csv')
        concat = pd.DataFrame()
        for file_name in list_csv:
            temp = pd.read_csv(file_name, sep=',', encoding='utf-8', index_col=0)
            concat = pd.concat([concat, temp])
        concat.sort_values(by=['date'], inplace=True)
        concat.to_csv(f'./{rename}.csv')
        return templates.TemplateResponse("rename.html", {"request": request, "keyword": keyword, "rename":rename})
    except Exception as ex:
        return print('error'), templates.TemplateResponse("error.html", {"request": request, "keyword": keyword, "rename":rename})



