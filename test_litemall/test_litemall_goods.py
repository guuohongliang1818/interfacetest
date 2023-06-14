# 姓名：郭宏亮
# 时间：2023/6/13 20:57
import jsonpath
import requests

from utils.schema_util import SchemaUtil


class TestLitemallGoods:
    _url_token = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
    _url_add = "https://litemall.hogwarts.ceshiren.com/admin/goods/create"
    _url_list = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
    _url_delete = "https://litemall.hogwarts.ceshiren.com/admin/goods/delete"
    _good_name = "Hogwarts_ghl_20230614"

    # 获取token
    def setup_class(self):
        r = requests.post(self._url_token,
                          json={"username": "hogwarts", "password": "test12345"})
        self.headers = {"X-Litemall-Admin-Token": jsonpath.jsonpath(r.json(), "$..token")[0]}

    def test_add(self):
        json_data = {
            "goods": {
                "picUrl": "",
                "gallery": [],
                "isHot": True,
                "isNew": True,
                "isOnSale": True,
                "goodsSn": "12491264512421",
                "name": self._good_name,
                "counterPrice": "8888"
            },
            "specifications": [
                {
                    "specification": "规格",
                    "value": "标准",
                    "picUrl": ""
                }
            ],
            "products": [
                {
                    "id": 0,
                    "specifications": [
                        "标准"
                    ],
                    "price": 0,
                    "number": 0,
                    "url": ""
                }
            ],
            "attributes": [
                {
                    "attribute": "材质",
                    "value": "纯棉"
                }
            ]
        }
        r = requests.post(self._url_add, json=json_data, headers=self.headers)
        print(r.text)
        assert r.json().get("errmsg") == "成功"
        # 需要结合数据库完成数据断言，断言查询语句的返回结果部位none即可
        # 或者调用查询接口进行断言
        r = requests.get(self._url_list,
                         params={"name": self._good_name},
                         headers=self.headers)
        print(r.text)
        assert jsonpath.jsonpath(r.json(), "$..name")[0] == self._good_name

    def test_list(self):
        r = requests.get(self._url_list,
                         params={"name": self._good_name},
                         headers=self.headers)
        print(r.text)
        assert r.json().get("errmsg") == "成功"
        assert jsonpath.jsonpath(r.json(), "$..name")[0] == self._good_name
        assert SchemaUtil.schema_validate_file("jsonschema.json", r.json())

    def test_delete(self):
        r = requests.post(self._url_delete,
                          json={"id": 1436720},
                          headers=self.headers)
        print(r.text)
        assert r.json().get("errmsg") == "成功"
