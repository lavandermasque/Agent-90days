# demo.py = 一组接口

from fastapi import APIRouter
router = APIRouter()

@router.get("/ping")
def ping():
    return {"msg": "pong"}

@router.get("/echo")
def echo(msg: str):
    return {"echo": msg}

@router.post("/sum")
def calc_sum(data: dict):
    return {"result": data["a"] + data["b"]}

