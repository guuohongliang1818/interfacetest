# 姓名：郭宏亮
# 时间：2023/6/15 22:25
import requests
import xmltodict
from requests import Response


class TestXml:

    def response_to_xml(self, response: Response):
        text = response.text
        if text.startswith("<?xml"):
            result = xmltodict.parse(response.text)
        elif text.startswith("{"):
            result = response.json()
        else:
            result = response
        return result

    def test_json_res(self):
        res = requests.get("https://httpbin.ceshiren.com/get")
        print(res)

    def test_xml_res(self):
        """
        xml转换为json
        :return:
        """
        res = requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
        print(self.response_to_xml(res))
