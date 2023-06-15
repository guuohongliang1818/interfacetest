# 姓名：郭宏亮
# 时间：2023/6/14 21:48
import os

import jsonpath
import pytest

from api.goods_api import GoodsApi
from utils.schema_util import SchemaUtil


class TestGoodsApi:
    def setup_class(self):
        self.goods_api = GoodsApi()

    @pytest.mark.parametrize("goods_name", ["ghl_1234567", "nibi_hhohoho"])
    def test_create(self, goods_name):
        json_data = {
            "goods": {
                "picUrl": "",
                "gallery": [],
                "isHot": True,
                "isNew": True,
                "isOnSale": True,
                "goodsSn": "12491264512421",
                "name": goods_name,
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
        create_json = self.goods_api.create(json_data)
        assert create_json.get("errmsg") == "成功"

        query_json = self.goods_api.list(goods_name)
        assert SchemaUtil.schema_validate_file("jsonschema.json", query_json)
        # 断言商品名称
        assert goods_name == jsonpath.jsonpath(query_json, "$..name")[0]
        # 获取商品的id
        delete_id = jsonpath.jsonpath(query_json, "$..id")[0]
        delete_json = self.goods_api.delete(delete_id)
        assert delete_json.get("errmsg") == "成功"

    def test_list(self):
        r = self.goods_api.list("Hogwarts_ghl_20230614")
        assert SchemaUtil.schema_validate_file("jsonschema.json", r)

    def test_delete(self):
        self.goods_api.delete(1436786)

    def test_get_env(self):
        assert os.getenv("litemall_env") == "test"
        print("java", os.getenv("JAVA_HOME"))
        print(os.getenv("litemall_env"))
