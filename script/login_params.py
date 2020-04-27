# 导包
import unittest
from api.login_api import LoginApi
import logging
from utils import assert_common_utils, read_login_data
import requests
from parameterized.parameterized import parameterized
# 创建登录的测试类,并继承unittest.TestCase
class TestLogin(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 创建登录的测试函数

    @parameterized.expand(read_login_data())
    def test01_login(self,mobile,password,http_code,success,code,message):
        # 调用登录接口
        response1 = self.login_api.login(mobile,password)
        # 打印结果
        logging.info("参数化登录结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self,response1,http_code,success,code,message)