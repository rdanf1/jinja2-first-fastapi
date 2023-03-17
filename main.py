# fastapi
# uvicorn
# python-multipart
# jinja2

import os

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 실행경로가 다르더라도 정확한 주소를 받기 위해 사용
# Use to get the correct address even if the execution path is different
main_dir = os.path.dirname(__file__)

app = FastAPI()

# 템플릿과 스태틱 파일 가져오기
# Import templates and static files
# Original structure
# templates = Jinja2Templates(directory=f"{main_dir}/templates")
# Migration of php site html part (we hard link to its src directory on same server)
templates = Jinja2Templates(directory=f"{main_dir}/src")
app.mount(
    "/static", StaticFiles(directory=f"{main_dir}/static"), name="static")

# Original structure
#@app.get("/")
#async def test(request: Request):
#    return templates.TemplateResponse("test.html", {"request": request, "data": "Test"})
# DR - Migration's
#my_list = ['/','/src/','/src/index.html']
#my_list = ["/"]
#for text in my_list:

@app.get("/")
async def test( request: Request ):
    return templates.TemplateResponse("test.html", {"request": request, "data": "Test"})
"""
@app.get("/src/css/styles.css")
async def styles():
    return templates.TemplateResponse("css/styles.css")
"""
# read as text/html => error
#@app.get("/src/js/script.js")
#async def test(request: Request):
#    return templates.TemplateResponse("js/script.js")


@app.post("/result")
async def test(idx: int = Form()):
    return {"idx": idx}


# 패키지 경로를 정확히 하기 위해서 아래방식으로 실행
# Run it in the following way to correct the package path
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
