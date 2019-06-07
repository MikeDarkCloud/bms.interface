# -*-coding:utf-8-*-
'''
配置文件--配置公共参数
'''
import os
def url():
    # url = 'http://bms-3.yzwill.cn/'
    url = 'http://bms.yzwill.cn/'
    return url

def path_log():
    pwd = os.getcwd()
    p1 = os.path.dirname(os.path.abspath('.'))
    p2 = "test_reprot\log"
    path = os.path.join(pwd, p2)
    return path

def path_xlexcel():
    pwd = os.getcwd()
    p1 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    p2 = "test_data\Excel_File\ApiStudentBaseInfo.xlsx"
    #调试用
    # path = os.path.join(p1, p2)
    #正式用
    path = os.path.join(pwd, p2)
    return path

def path_case():
    pwd = os.getcwd()
    p2 = "test_case"
    path = os.path.join(pwd, p2)
    return path

def path_report():
    pwd = os.getcwd()
    p1 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    p2 = "test_report\\report"
    path = os.path.join(pwd, p2)
    return path


def path_jpg():
    pwd = os.getcwd()
    p1 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    p2 = "test_data\\jpg\\1.jpg"
    #调试用
    # path = os.path.join(p1, p2)
    #正式用
    path = os.path.join(pwd, p2)
    return path