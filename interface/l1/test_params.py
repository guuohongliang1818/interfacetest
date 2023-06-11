# 姓名：郭宏亮
# 时间：2023/6/11 15:40
import requests


def test_params_one():
    r = requests.get("https://httpbin.ceshiren.com/get?teacher=AD&age=18")
    # 查看相应信息
    print("====", r.text)


def test_params_two():
    r = requests.request("get", "https://httpbin.ceshiren.com/get?teacher=AD&age=18")
    # 查看相应信息
    print("====", r.text)


def test_params_three():
    # 前提条件
    # params 要求传入是一个字典
    dic = {"teacher": "ghl", "age": 15}
    r = requests.get("https://httpbin.ceshiren.com/get", params=dic)
    print(r.text)
