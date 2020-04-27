# 导包
import unittest
from api.login_api import LoginApi
import logging
from utils import assert_common_utils
import requests
# 创建登录的测试类,并继承unittest.TestCase
class TestLogin(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 创建登录的测试函数

    # 测试登录成功
    def test01_login_success(self):
        # 调用登录接口
        response1 = self.login_api.login("13800000002","123456")
        # 打印结果
        logging.info("登录结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self,response1,200,True,10000,"操作成功")

    # 测试用户名不存在
    def test02_username_is_not_exist(self):
        # 调用登录接口
        response1 = self.login_api.login("19900000002", "123456")
        # 打印结果
        logging.info("用户名不存在结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, False, 20001, "用户名或密码错误")


    # 测试密码错误
    def test03_password_is_error(self):
        # 调用登录接口
        response1 = self.login_api.login("13800000002", "1234567")
        # 打印结果
        logging.info("密码错误结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, False, 20001, "用户名或密码错误")


    # 测试无参
    def test04_none_params(self):
        response1 = requests.post("http://182.92.81.159/api/sys/login")
        # 打印结果
        logging.info("无参结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, False, 99999, "抱歉,系统繁忙,请稍后重试")

    # 测试用户名为空
    def test05_username_is_empty(self):
        # 调用登录接口
        response1 = self.login_api.login("", "1234567")
        # 打印结果
        logging.info("用户名为空结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, False, 20001, "用户名或密码错误")

    # 测试密码为空
    def test06_password_is_empty(self):
        # 调用登录接口
        response1 = self.login_api.login("13800000002", "")
        # 打印结果
        logging.info("密码为空结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少mobile
    def test07_less_mobile(self):
        response1 = self.login_api.login_params({"password":"123456"})
        # 打印结果
        logging.info("缺少mobile结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少password
    def test08_less_password(self):
        response1 = requests.post("http://182.92.81.159/api/sys/login",
                                  json={"mobile":"13800000002"})
        # 打印结果
        logging.info("缺少password结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, False, 20001, "用户名或密码错误")


    # 多参-增加1个参数
    def test09_add_params(self):
        response1 = requests.post("http://182.92.81.159/api/sys/login",
                                  json={"mobile": "13800000002",
                                        "password":"123456",
                                        "a":"123"})
        # 打印结果
        logging.info("增加1个参数结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, True, 10000, "操作成功")
    # 错误参数
    def test10_error_params(self):
        response1 = requests.post("http://182.92.81.159/api/sys/login",
                                  json={"mbile": "13800000002",
                                        "password": "123456"})
        # 打印结果
        logging.info("错误参数数结果为:{}".format(response1))
        # 断言登录结果
        assert_common_utils(self, response1, 200, True, 10000, "操作成功")