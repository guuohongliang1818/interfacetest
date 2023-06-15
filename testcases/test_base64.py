# 姓名：郭宏亮
# 时间：2023/6/15 22:59
import base64

import jsonpath
import requests


class TestBase64:
    secret_msg = base64.b64encode("霍格沃兹".encode("utf-8"))

    def test_base64(self):
        print(self.secret_msg)
        url = "https://httpbin.ceshiren.com/post"
        data = {"msg": self.secret_msg}
        res = requests.post(url, data=data)
        print(res.text)

        msg = jsonpath.jsonpath(res.json(), "$..msg")[0]
        print("msg：", msg)
        # 对获取的加密数据进行解密, 如果有中文需要再调.decode('utf-8')
        encode_str = base64.b64decode(msg).decode("utf-8")
        assert encode_str == "霍格沃兹"
