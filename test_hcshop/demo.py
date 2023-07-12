import jsonpath
import requests

data = {
    "accounts": "15022195606",
    "pwd": "ghl627129",
    "type": "username"
}

# 写法1
res = requests.post(
    url="http://shop-xo.hctestedu.com/index.php?s=/api/user/login&application=app&application_client_type=weixin",
    json=data)
print(res.text)
print("token：", jsonpath.jsonpath(res.json(), "$..token")[0])
