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

2. 인덱스 페이지

       @app.get("/") async def root(request: Request):
       return templates.TemplateResponse("index.html", {"request": request})
     
      get 메서드를 이용하여 index.html로 연결
      
3. 크롤링 페이지

       @app.get("/scrap/{keyword}", response_class=HTMLResponse)
       async def 수집하기(request: Request, keyword:str):
      처음엔 post메서드로 입력을 받고 크롤링 하려고 하였으나 주소접속시 바로 크롤링 되도록 변경함

4. 수정 페이지

       @app.get("/rename/{keyword}/{rename}", response_class=HTMLResponse)
       async def 다른이름으로저장(request: Request, keyword: str, rename: str):
      파일을 get메서드로 불러들인 후에 다른이름으로 저장할 수 있도록 만듦.

## 참조
  https://velog.io/@idj7183/Fast-API-%ED%99%9C%EC%9A%A9-2
  블로그 dongjin im
  
  https://fastapi.tiangolo.com/
  공식

