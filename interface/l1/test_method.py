# 姓名：郭宏亮
# 时间：2023/6/11 15:33
import requests


def test_get():
    r = requests.get("https://httpbin.ceshiren.com/get")
    print(r)


def test_post():
    r = requests.post("https://httpbin.ceshiren.com/post")
    print(r)


def test_delete():
    r = requests.delete("https://httpbin.ceshiren.com/delete")
    print(r)


def test_put():
    r = requests.put("https://httpbin.ceshiren.com/put")
    print(r)


def test_request():
    r = requests.request("get", "https://httpbin.ceshiren.com/get")
    print(r)
