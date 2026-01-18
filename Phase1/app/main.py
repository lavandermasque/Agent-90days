"""
from utils import safe_int

def main():
    user_input = input("请输入一个数字：")
    result = safe_int(user_input)
    if result is None:
        print("❌输入的不是一个有效数字")
    else:
        print(f"✅你输入的数字是{result}")

if __name__ == "__main__":
    main()
"""
from fastapi import FastAPI
from app.routers import demo

app = FastAPI()
app.include_router(demo.router)