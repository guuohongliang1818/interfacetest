# 姓名：郭宏亮
# 时间：2023/6/12 15:01
import requests


def test_file():
    # 通过charles代理获取请求，查看请求的参数，返回
    proxy = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }
    r = requests.post("https://httpbin.ceshiren.com/post",
                      proxies=proxy,
                      verify=False,
                      files={"test_file": open("hello.txt", "rb")})
    print(r.text)
