# 导包

from api.login import LoginAPI


# 创建测试类
class TestLoginAPI:
    uuid = None

    # 前置处理
    def setup_method(self):
        # 实例化
        self.login_api = LoginAPI()
        # 验证码
        response = self.login_api.get_verify_code()
        # 提取验证码
        TestLoginAPI.uuid = response.json().get("uuid")
        print(TestLoginAPI.uuid)

    def teardown_method(self):
        pass

    # 登录成功
    def test01_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert '成功' in response.text
        # 断言响应JSON数据中的code值
        assert 200 == response.json().get("code")

    # 登录失败（用户名为空）
    def test02_without_username(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含错误
        assert '错误' in response.text
        # 断言响应JSON数据中的code值
        assert 500 == response.json().get("code")

    # 登录失败（未注册用户）
    def test03_username_not_exist(self):
        login_data = {
            "username": "jack888",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含错误
        assert '错误' in response.text
        # 断言响应JSON数据中的code值
        assert 500 == response.json().get("code")
