from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

# 1. 接口1: GET+Query参数
@app.get("/echo")
def echo(msg: str):
    return {
        "you_said": msg
    }

# 2. GET + Path参数
@app.get("/post/{post_id}")
def get_post(post_id: int):
    return {
        "post_id": post_id
    }

# 3. POST + JSON Body = 把一个结构化的数据对象传给后端函数
# POST本质：HTTP请求 = 在远程调用一个Python函数
# POST请求形式（json）：{
#   "text": "This is a test input"
# }
from pydantic import BaseModel
class TextIn(BaseModel):
    text: str

@app.post("/summerize")
def summerize(data: TextIn):
    text = data.text
    return {
        "original_length": len(text),
        "preview": text[:50]
    }
