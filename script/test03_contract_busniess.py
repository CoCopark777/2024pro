# 导包
from api.login import LoginAPI
from api.course import CourseAPI

# 创建测试类
class TestContractBusiness:
    token = None
    #前置处理
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

    #后置处理
    def teardown_method(self):
        pass
    # 1.登录成功
    def test01_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.json().get("uuid"))

        # 登录成功
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
        TestContractBusiness.token = res_l.json().get("token")
        print(TestContractBusiness.token)

    # 2.课程新增成功
    def test02_add_course(self):
        add_data = {"name":"测试开发课", "subject":"6", "price":899, "applicablePerson":"2", "info":"测试开发课"}
        response = self.course_api.add_course(test_data=add_data, token=TestContractBusiness.token)
        print(response.json())
