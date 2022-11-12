# fastapi_crawing


## Description
FastApi 활용 크롤링 서버 구축
 
## FastApi란
Sebastián Ramírez란 사람이 만든 파이썬 기반 오픈소스 웹 프레임워크
파이썬 기반 웹프레임워크 중에서 가장 빠른 프레임워크 중 하나

## code
1. FastAPi 실행 code

       app = FastAPI()
    
app으로 정의한 뒤에 메서드를 불러들임

3. 인덱스 페이지

       @app.get("/") async def root(request: Request):
       return templates.TemplateResponse("index.html", {"request": request})
     
     get 메서드를 이용하여 index.html로 연결
5. 



2. 


## 과제 중 어려운 점
