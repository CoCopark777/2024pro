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

    # 课程删除成功
    def test01_delete_course(self):
        response = self.course_api.delete_course(course_id=23056458704342213, token=TestAddCourseAPI.token)
        print(response.json())
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert "成功" in response.text
        # 断言响应JSON数据中的code值
        assert 200 == response.json().get("code")

    # 课程删除失败(id不存在)

    def test02_delete_fail_id_exist(self):
        response = self.course_api.delete_course(course_id=000, token=TestAddCourseAPI.token)
        print(response.json())
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert "操作失败" in response.text
        # 断言响应JSON数据中的code值
        assert 500 == response.json().get("code")

    # 课程删除失败（用户未登录）
    def test03_delete_fail(self):
        response = self.course_api.delete_course(course_id=111, token="XXX")
        print(response.json())
        # 断言状态码200
        assert 200 == response.status_code
        # 断言响应信息包含成功
        assert "认证失败" in response.text
        # 断言响应JSON数据中的code值
        assert 401 == response.json().get("code")
