from http.client import responses

import requests
print(requests.__version__)

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url) # 发一个GET请求

print(response.status_code)
print(response.text)

# 解析JSON为Python数据（dict/list）
data = response.json()
print(type(data))
print(data)
print(data["title"])
print(data["id"])

# 工程思维：函数化、容错、通用性
def fetch_post(post_id):
    # 获取指定post_id的内容
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    return resp.json()

post = fetch_post(1)
print(post["title"])

def get_titles(limit=5):
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = resp.json() #转为dict格式
    return [p["title"] for p in posts[:limit]]

print(get_titles())
