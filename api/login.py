# 接口信息
# 验证码
# 地址：http://kdtx-test.itheima.net/api/captchaImage
# 方法：get

# 登录
# 地址 http://kdtx-test.itheima.net/api/login
# 请求数据
# 请求头 Content-Type": "application/json
# 请求体 {"username":"admin", "password":"HM_2023_test","code":2, "uuid":"9d4408f3f9c04f0986de8a0e8d1ed1ef" }

# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的，接口方法被调用时需要返回对应的响应结果

#导包
import requests

#创建接口类
class LoginAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        self.url_verify = "http://kdtx-test.itheima.net/api/captchaImage"
        self.url_login = "http://kdtx-test.itheima.net/api/login"

    # 验证码
    def get_verify_code(self):
        return requests.get(url=self.url_verify)

    # 登录
    def login(self, test_data):
        return requests.post(url=self.url_login, json=test_data)