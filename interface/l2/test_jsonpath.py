# 姓名：郭宏亮
# 时间：2023/6/11 18:29
import jsonpath
import requests


def test_jsonpath():
    r = requests.post("https://httpbin.ceshiren.com/post",
                      json={"name": [{"age": 18}]})

    print(r.text)
    print(jsonpath.jsonpath(r.json(), "$..age")[0])
