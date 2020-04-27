# 导包
import logging
import unittest
from utils import assert_common_utils, DBUtils, read_add_emp, read_query_emp, read_modify_emp, read_delete_emp
from api.emp_login import EmployeeApi
import app
import pymysql
from parameterized.parameterized import parameterized

# 创建测试类继承unittest.TestCase
class TestEmployee(unittest.TestCase):

    # 实例化unittest的函数
    def setUp(self):
        # 实例化
        self.emp_aip = EmployeeApi()

    def tearDown(self):
        pass



    def test01_login_success(self):
        # 调用登录接口
        response1 = self.emp_aip.login("13800000002", "123456")
        # 打印登陆结果
        logging.info("员工模块的登录结果为:{}".format(response1.json()))
        # 取出令牌,并拼接成以Bearer 开头的字符串
        token = "Bearer" + response1.json().get('data')
        logging.info("取出的令牌为:{}".format(token))
        # 设置员工模块所需要的请求头
        headers1 = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers1
        logging.info("员工模块请求头为:{}".format(app.HEADERS))

    @parameterized(read_add_emp())
    def test02_add_emp(self,username,mobile,http_code,success,code,message):
        # 调用添加员工
        response_add_emp = self.emp_aip.add_emp(username, mobile, app.HEADERS)
        logging.info("添加员工接口结果为:{}".format(response_add_emp))
        # 断言结果: 响应状态码,success,code,message
        assert_common_utils(self, response_add_emp, http_code, success, code, message)

        # 保存员工ID给后续使用
        emp_id = response_add_emp.json().get("data").get("id")
        app.EMPID = emp_id
        logging.info("保存的员工ID为:{}".format(app.EMPID))

    @parameterized(read_query_emp)
    def test03_query_emp(self,http_code,success,code,message):
        # 调用查询员工
        response_query = self.emp_aip.query_emp(app.EMPID, app.HEADERS)
        logging.info("查询员工的结果为:{}".format(response_query))
        # 断言结果: 响应状态码,success,code,message
        assert_common_utils(self, response_query, http_code, success, code, "message")

    @parameterized(read_modify_emp)
    def test04_modify_emp(self,username,http_code,success,code,message):
        # 调用修改员工
        response_modify = self.emp_aip.modify_emp(app.EMPID, username,app.HEADERS)
        logging.info("修改员工的结果为:{}".format(response_modify))

        # 建立连接
        with DBUtils() as db:

            # 执行SQL语句(根据添加员工返回的EMPID,查询数据库员工表表的username)
            # 查询语句
            SQL1 = "select username from bs_user where id={};".format(app.EMPID)
            logging.info("要查询的SQL语句为:{}".format(SQL1))
            # 执行语句
            db.execute(SQL1)
            # 获取结果
            result1 =db.fetchone()
            logging.info("SQL查询出来的结果为:{}".format(result1))
            # 断言修改结果是否正确
            self.assertEqual(username,result1[0])


        # 断言结果: 响应状态码,success,code,message
        assert_common_utils(self, response_modify, http_code, success, code, message)

    @parameterized(read_delete_emp)
    def test06_delete_emp(self,http_code,success,code,message):
        # 调用删除员工
        response_delete = self.emp_aip.delete_emp(app.EMPID,app.HEADERS)
        logging.info("删除员工的结果为:{}".format(response_delete))
        # 断言结果: 响应状态码,success,code,message
        assert_common_utils(self, response_delete, http_code, success, code, message)