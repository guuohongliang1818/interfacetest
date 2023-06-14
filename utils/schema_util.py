# 姓名：郭宏亮
# 时间：2023/6/13 22:15
import json
import os
import sys

from genson import SchemaBuilder
from jsonschema.validators import validate


class SchemaUtil:
    # 安装：pip install genson
    @classmethod
    def generate_jsonschema(cls, obj):
        # 实例化jsonschem
        builder = SchemaBuilder()
        # 传入被转换的对象
        builder.add_object(obj)
        # 转换成 schema 数据
        return builder.to_schema()

    @classmethod
    def generate_jsonschema_file(cls, file, obj):
        jsonschema = cls.generate_jsonschema(obj)
        with open(file, "w") as f:
            json.dump(jsonschema, f)

    # 安装：pip install jsonschema
    @classmethod
    def schema_validate(cls, obj, schema):
        '''
        对比 python 对象与生成的 JSONSchame 的结构是否一致
        '''
        try:
            validate(instance=obj, schema=schema)
            return True
        except Exception as e:
            return False

    @classmethod
    def schema_validate_file(cls, file, obj):
        print(os.path.abspath(file))
        # 路径优化
        print(os.path.join(os.path.dirname(os.path.abspath(__file__)), file))
        # 从文件中获取schema数据
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file), "r") as f:
            schema = json.load(f)
        return cls.schema_validate(obj, schema)


if __name__ == '__main__':
    data = {"errno": 0, "data": {"total": 1, "pages": 1, "limit": 10, "page": 1, "list": [
        {"id": 1436721, "goodsSn": "12491264512421", "name": "Hogwarts_ghl_20230613", "categoryId": 0, "brandId": 0,
         "gallery": [], "keywords": "", "brief": "", "isOnSale": True, "sortOrder": 100, "picUrl": "", "isNew": True,
         "isHot": True, "unit": "’件‘", "counterPrice": 8888.00, "retailPrice": 100,
         "addTime": "2023-06-13 13:53:49",
         "updateTime": "2023-06-13 13:53:49", "deleted": False}]}, "errmsg": "成功"}

    # SchemaUtil.generate_jsonschema_file("jsonschema.json", data)
    value = SchemaUtil.schema_validate_file("jsonschema.json", data)
    print(value)
