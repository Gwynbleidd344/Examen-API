from urllib import request

from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
def hello_page():
    with open("Hello.html","r",encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")
