# 合同上传

"""
URL： http://kdtx-test.itheima.net/api/common/upload
方法：Post
请求数据：
请求头{"Content-Type": "multipart/from-data", "Authorization": "xxx"}
请求体:{"file": "合同文件"}

"""

import requests
import config


class ContractAPI:
    # 初始化
    def __init__(self):
        # self.url_upload = "http://kdtx-test.itheima.net/api/common/upload"
        # self.url_add_contract = "http://kdtx-test.itheima.net/api/contract"
        self.url_upload = config.BASE_URL + "/api/common/upload"
        self.url_add_contract = config.BASE_URL + "/api/contract"

    # 合同上传接口
    def upload_contract(self, test_data, token):
        return requests.post(url=self.url_upload, files={"file": test_data}, headers={"Authorization": token})

    # 合同新增接口
    def add_contract(self, test_data, token):
        return requests.post(url=self.url_add_contract, json=test_data, headers={"Authorization": token})
