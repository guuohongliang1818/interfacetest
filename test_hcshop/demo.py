import jsonpath
import requests

# http://shop-xo.hctestedu.com/
# 华测账号和密码：15022195606，ghl627129
data = {
    "accounts": "15022195606",
    "pwd": "ghl627129",
    "type": "username"
}

# 写法1
res = requests.post(
    url="http://shop-xo.hctestedu.com/index.php?s=/api/user/login&application=app&application_client_type=weixin",
    data=data)
print(res.text)
print("写法一token：", jsonpath.jsonpath(res.json(), "$..token")[0])
print("================================================================")
# 写法2
paramData = {
    "application": "app",
    "application_client_type": "weixin"
}
res1 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=/api/user/login", params=paramData, json=data)
print(res1.text)
print("写法一token：", jsonpath.jsonpath(res1.json(), "$..token")[0])

print("paramData", paramData)
