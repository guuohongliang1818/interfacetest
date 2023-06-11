# 姓名：郭宏亮
# 时间：2023/6/11 15:59
import requests


def test_headers():
    r = requests.get("https://httpbin.ceshiren.com/get",
                     params={"name": "ghl", "age": 18},
                     headers={"user-agent": "my-app/0.0.1", "Host1": "ADD", "name": "ghl"})

    print(r.text)
