# demo.py = 一组接口

from fastapi import APIRouter, UploadFile, File
router = APIRouter()

# 当通过浏览器或程序访问 /ping 这个网址，并且用的是 GET 方法，运行ping()
@router.get("/ping")
def ping():
    return {"msg": "pong"}

# 访问：http://.../echo?msg=value
@router.get("/echo")
def echo(msg: str):
    return {"echo": msg}

# 一个程序发送 POST 请求到 /sum，并附带数据
@router.post("/sum")
def calc_sum(data: dict):
    return {"result": data["a"] + data["b"]}

@router.post("/upload_file")
def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }