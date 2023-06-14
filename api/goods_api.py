# 姓名：郭宏亮
# 时间：2023/6/14 21:35
import jsonpath
import requests

from api.litemall_api import LiteMallApi


class GoodsApi(LiteMallApi):
    _url_add = "admin/goods/create"
    _url_list = "admin/goods/list"
    _url_delete = "admin/goods/delete"

    def create(self, json_data):
        return self.send_request("post", self._url_add, json=json_data, headers={"name": "AD"})

    def list(self, goods_name):
        return self.send_request("get", self._url_list, params={"name": goods_name}, headers={"name": "AD"})

    def delete(self, delete_id):
        return self.send_request("post", self._url_delete, json={"id": delete_id}, headers={"name": "AD"})
