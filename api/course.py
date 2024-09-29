# 课程模块接口封装，核心在于依据接口文档实现接口信息封装，重点关注接口如何被调用

# 接口信息
"""
URL: http://kdtx-test.itheima.net/api/clues/course
方法：Post
请求数据：
请求头{"Content-Type": "application/json", "Authorization": "xxx"}
请求体:{"name":"测试开发课", "subject":"6", "price":899, "applicablePerson":"2", "info":"测试开发课"}
"""


# 导包
import requests

# 创建接口类
class CourseAPI:
    # 初始化
    def __init__(self):
        self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"

    # 课程添加
    def add_course(self,test_data, token):
        return requests.post(url=self.url_add_course, json=test_data, headers={"Authorization":token})



