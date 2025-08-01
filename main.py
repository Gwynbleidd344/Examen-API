from datetime import datetime
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

class PostModel(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

posts_list: List[PostModel] = []

def serialized_posts_list():
    post_converted = []
    for post in posts_list:
        post_converted.append(post.model_dump())
    return post_converted

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
def pong():
    return (Response("pong",status_code=200))

@app.get("/ping/auth")
def pong_auth(request: Request):
    auth = request.headers.get("Authorization")
    if auth != "Basic YWRtaW46MTIzNDU2Nw==":
        return (Response("unauthorized",status_code=401))
    else:
        return (Response("pong",status_code=200))


@app.get("/home")
def home():
    with open("welcome.html", "r",encoding="utf-8") as welcome:
        html_content = welcome.read()
    return Response(content=html_content, status_code=200 ,media_type="text/html")

@app.get("/posts")
def get_posts():
    return JSONResponse(content={"posts":serialized_posts_list()}, status_code=200)

@app.post("/posts")
def add_posts(new_post: List[PostModel]):
    posts_list.extend(new_post)
    return JSONResponse(content={"posts":serialized_posts_list()}, status_code=201)

@app.put("/posts")
def update_posts(incoming_info: List[PostModel]):
    for incoming in incoming_info:
        for post in posts_list:
            if post.title == incoming.title:
                post.title = incoming.title
                post.author = incoming.author
                post.content = incoming.content
                post.creation_datetime = incoming.creation_datetime
    return JSONResponse(content={"posts":serialized_posts_list()}, status_code=200)

@app.get("/{invalid_path}")
def invalid_path(invalid_path:str):
    with open("404.html", "r",encoding="utf-8") as not_found:
        html_content = not_found.read()
    return Response(content=html_content, status_code=404 ,media_type="text/html")

