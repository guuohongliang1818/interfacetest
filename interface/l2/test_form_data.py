# 姓名：郭宏亮
# 时间：2023/6/11 16:53
import requests


def test_form_data():
    # Content-Type 为 application/x-www-form-urlencoded
    r = requests.post("https://httpbin.ceshiren.com/post",
                      # params={"data": "urlData"},
                      data={"name": "郭宏亮", "age": 18})
    print(r.text)
    assert r.status_code == 200
    # r.json()，自动把响应体转成json
    print(r.json().get("url"))
    assert "https://httpbin.ceshiren.com/post" == r.json().get("url")
