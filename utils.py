# 自定义工具类
import json
import os

import pymysql
# 封装通用断言函数
def assert_common_utils(self,response,http_code,success,code,message):
    # 断言结果: 响应状态码,success,code,message
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

# 封装数据库
class DBUtils:

    # 初始化类时,要运行的代码
    def __init__(self,host='182.92.81.159',user='readuser',password='iHRM_user_2019',database='iherm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 使用with语法时,进入函数会先运行enter代码
    def __enter__(self):
        # 与数据库建立连接
        self.conn = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        # 获取游标
        self.cursor = self.conn.cursor()
        return self.cursor

    # 退出with语法时,会先运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标和关闭连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

def read_login_data():
    # 定义数据文件路径
    login_data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/login.json"
    # 读取数据文件
    with open(login_data_path) as f:
        # 使用json模块加载数据为json格式
        jsonData = json.load(f)

        # 定义一个result_list用于存放读取的数据
        result_list = []

        # 遍历jsonData,提取要读取的数据
        for case_data in jsonData:
            # 获取读取数据当中的mobile数据
            mobile = case_data.get('mobile')
            password = case_data.get('password')
            http_code = case_data.get('http_code')
            success = case_data.get('success')
            code = case_data.get('code')
            message = case_data.get('message')
            result_list.append((mobile,password,http_code,success,code,message))
            # result_list.append(tuple(case_data.values()))

    return result_list


def read_add_emp():
    # 读取数据
    emp_path = os.path.dirname(os.path.abspath(__file__)) + "/data/employee.json"
    with open(emp_path,mode='r',encoding='utf-8') as f:
        # 使用json加载数据
        jsonData = json.load(f)
        # 定义结果变量来存放读取的数据
        result_list = []
        # 把数据存放在结果中
        add_emp_data = jsonData.get('add_emp')  # 读取json 文件中添加员工的数据

        username = add_emp_data.get('username')  # 读取add_emo_data 中的username 数据
        mobile = add_emp_data.get('mobile')
        http_code = add_emp_data.get('http_code')
        success = add_emp_data.get('success')
        code = add_emp_data.get('code')
        message = add_emp_data.get('message')

        result_list.append((username,mobile,http_code,success,code,message))

    return result_list

def read_query_emp():
    # 读取数据
    emp_path = os.path.dirname(os.path.abspath(__file__)) + "/data/employee.json"
    with open(emp_path,mode='r',encoding='utf-8') as f:
        # 使用json加载数据
        jsonData = json.load(f)
        # 定义结果变量来存放读取的数据
        result_list = []
        # 把数据存放在结果中
        query_emp_data = jsonData.get('query_emp')  # 读取json 文件中添加员工的数据

        http_code = query_emp_data.get('http_code')
        success = query_emp_data.get('success')
        code = query_emp_data.get('code')
        message = query_emp_data.get('message')

        result_list.append((http_code,success,code,message))

    return result_list


def read_modify_emp():
    # 读取数据
    emp_path = os.path.dirname(os.path.abspath(__file__)) + "/data/employee.json"
    with open(emp_path,mode='r',encoding='utf-8') as f:
        # 使用json加载数据
        jsonData = json.load(f)
        # 定义结果变量来存放读取的数据
        result_list = []
        # 把数据存放在结果中
        modify_emp_data = jsonData.get('modify_emp')  # 读取json 文件中添加员工的数据

        username = modify_emp_data.get('username')
        http_code = modify_emp_data.get('http_code')
        success = modify_emp_data.get('success')
        code = modify_emp_data.get('code')
        message = modify_emp_data.get('message')

        result_list.append((username,http_code,success,code,message))

    return result_list


def read_delete_emp():
    # 读取数据
    emp_path = os.path.dirname(os.path.abspath(__file__)) + "/data/employee.json"
    with open(emp_path,mode='r',encoding='utf-8') as f:
        # 使用json加载数据
        jsonData = json.load(f)
        # 定义结果变量来存放读取的数据
        result_list = []
        # 把数据存放在结果中
        delete_emp_data = jsonData.get('delete_emp')  # 读取json 文件中添加员工的数据

        http_code = delete_emp_data.get('http_code')
        success = delete_emp_data.get('success')
        code = delete_emp_data.get('code')
        message = delete_emp_data.get('message')

        result_list.append((http_code,success,code,message))

    return result_list

if __name__ == '__main__':
    read_login_data()