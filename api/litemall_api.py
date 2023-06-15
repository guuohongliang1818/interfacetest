# 姓名：郭宏亮
# 时间：2023/6/14 21:35
import os

import jsonpath
import requests


class LiteMallApi:
    _base_url = "https://litemall.hogwarts.ceshiren.com/"
    _url_token = "admin/auth/login"

    def __init__(self):
        r = requests.post(self._base_url + self._url_token,
                          json={"username": "hogwarts", "password": "test12345"})
        self.headers = {"X-Litemall-Admin-Token": jsonpath.jsonpath(r.json(), "$..token")[0]}

    def send_request(self, method, url, **kwargs):
        print(f"请求地址url为：{url}")
        print(f"请求参数为：{kwargs}")
        if kwargs.get("headers"):
            kwargs.get("headers").update(self.headers)
        else:
            kwargs["headers"] = self.headers
        print(f"修改之后的请求参数为：{kwargs}")
        r = requests.request(method, self._base_url + url, **kwargs)
        print(f"请求的返回结果为：{r.text}")
        return r.json()


if __name__ == '__main__':
    args = {'headers': {'name': 'AD'}, 'params': {'name': 'Hogwarts_ghl_20230614'}}
    print(bool(args.get("headers")))
    print(bool(args.get("ssss")))
    args.get("headers").update({"age": 12})
    print(args.get("headers"))
    print(os.getenv("litemall_env", default="test"))
