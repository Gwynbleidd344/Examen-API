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
    return Response("home",status_code=200)
