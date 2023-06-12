# 姓名：郭宏亮
# 时间：2023/6/11 18:08
import requests


def test_case1():
    r = requests.get("https://www.google.com/", timeout=3)
    print(r.text)
    assert r.status_code == 200


def test_case2():
    r = requests.get("https://httpbin.ceshiren.com/get")
    print(r.text)
    assert r.status_code == 200


def test_case3():
    r = requests.post("https://httpbin.ceshiren.com/post", data={"name": "张三", "age": 15})
    print(r.text)
