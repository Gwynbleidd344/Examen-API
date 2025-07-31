from urllib import response

from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
def pong():
    return Response("pong",status_code=200)


@app.get("/home")
def home():
    with open("welcome.html", "r",encoding="utf-8") as welcome:
        html_content = welcome.read()
    return Response(content=html_content, status_code=200 ,media_type="text/html")

@app.get("/{invalid_path}")
def invalid_path(invalid_path:str):
    with open("404.html", "r",encoding="utf-8") as not_found:
        html_content = not_found.read()
    return Response(content=html_content, status_code=404 ,media_type="text/html")

