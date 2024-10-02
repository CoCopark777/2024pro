from api.login import LoginAPI
from api.course import CourseAPI


class TestAddCourseAPI:
    token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

        # 获取验证码
        res_v = self.login_api.get_verify_code()
        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)
        TestAddCourseAPI.token = res_l.json().get("token")

    def teardown_method(self):
        pass

    def test01_success(self):
        add_data = {
            "name": "测试开发课1002",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2"
        }
        response = self.course_api.add_course(test_data=add_data, token=TestAddCourseAPI.token)
        print(response.json())
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert "成功" in response.text
        # 断言响应JSON数据中的code值
        assert 200 == response.json().get("code")

    def test02_fail(self):
        add_data = {
            "name": "测试开发课1002",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2"
        }
        response = self.course_api.add_course(test_data=add_data, token="XXX")
        print(response.json())
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert "认证失败" in response.text
        # 断言响应JSON数据中的code值
        assert 401 == response.json().get("code")