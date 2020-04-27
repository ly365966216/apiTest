# 导包
import requests
# 创建API类
class EmployeeApi:

    def __init__(self):
        pass

    # 实现封装登录接口
    def login(self, mobile, password):
            login_url = "http://182.92.81.159/api/sys/login"
            json_data = {"mobile": mobile, "password": password}
            return requests.post(login_url, json_data)

    # 实现封装添加员工接口
    def add_emp(self,username,mobile,headers1):
        add_emp_url = "http://182.92.81.159/api/sys/user"
        jsonData = {"username": username,"mobile": mobile}
        return requests.post(add_emp_url,json=jsonData,headers=headers1)

    # 实现封装查询员工接口
    def query_emp(self,emp_id,headers1):
        query_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.get(query_url, header=headers1)

    # 实现封装修改接口
    def modify_emp(self,emp_id,username,headers1):
        modify_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.put(modify_url,json={"username": username},header=headers1)

    # 实现封装删除接口
    def delete_emp(self,emp_id,headers1):
        delete_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.delete(delete_url,header=headers1)