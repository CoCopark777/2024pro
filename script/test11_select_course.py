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

    def test01_select_success(self):
        # 查询到数据太多报错，没有打印出来
        response = self.course_api.select_course(test_data="?测试开发提升课01", token=TestAddCourseAPI.token)
        print(response.text)
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert "成功" in response.text
        # 断言响应JSON数据中的code值
        assert 200 == response.json().get("code")

    # （未登录）
    def test02_select_fail(self):
        response = self.course_api.select_course(test_data="?subject=6", token="XXX")
        print(response.json())
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert "认证失败" in response.text
        # 断言响应JSON数据中的code值
        assert 401 == response.json().get("code")
