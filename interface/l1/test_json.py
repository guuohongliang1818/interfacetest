# 姓名：郭宏亮
# 时间：2023/6/11 16:14
import requests


def test_json():
    # Content-Type 为 application/json
    r = requests.post("https://httpbin.ceshiren.com/post",
                      # params={"data": "urlData"},
                      json={"name": "郭宏亮", "age": 18})
    print(r.text)
    assert r.status_code == 200
    # r.json()，自动把响应体转成json
    print(r.json().get("url"))
    assert "https://httpbin.ceshiren.com/post" == r.json().get("url")
