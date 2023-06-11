# 姓名：郭宏亮
# 时间：2023/6/11 17:02
import requests


def test_proxy():
    proxy = {
        # 协议名称：代理地址
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"}
    r = requests.post("https://httpbin.ceshiren.com/post",
                      # params={"data": "urlData"},
                      json={"name": "郭宏亮", "age": 18}, proxies=proxy, verify=False)
    print(r.text)
    assert r.status_code == 200
    # r.json()，自动把响应体转成json
    print(r.json().get("url"))
    assert "https://httpbin.ceshiren.com/post" == r.json().get("url")
