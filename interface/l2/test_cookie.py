# 姓名：郭宏亮
# 时间：2023/6/11 18:34
import requests


def test_cookie():
    r = requests.get("https://httpbin.ceshiren.com/get",
                     # 必须输str类型
                     cookies={"name": "ghl", "age": "199"})
    print(r.text)
