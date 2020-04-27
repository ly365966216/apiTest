# 配置全局变量,公有的配置函数或者类
# 1 导包
import logging
import os
from logging import handlers


# 获取当前项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 定义全局变量headers
HEADERS = {"Content-Type":"application/json"}

# 定义全部变量emp_id
EMPID = ""

# 2 定义一个初始化日志配置的函数:初始化日志的输出路径(例如:输出到控制和日志文件中)
def init_loggin():
    # 3 设置日志器
    logger = logging.getLogger()
    # 4 设置日志等级
    logger.setLevel(logging.INFO)
    # 5 创建处理器,通过处理控制日志的打印(打印到控制台和日志文件中)
    sh = logging.StreamHandler()

    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/ihrm.log",
                                                   when='s', interval=10,
                                                   backupCount=3, encoding='utf-8')
    # 6 设置日志的格式,所以需要创建格式和格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    fomatter = logging.Formatter(fmt)
    # 7 将格式化器添加到处理器当中
    sh.setFormatter(fomatter)
    fh.setFormatter(fomatter)
    # 8 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)