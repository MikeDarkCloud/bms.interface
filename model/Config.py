# -*-coding:utf-8-*-
'''
配置文件--配置公共参数
'''
import os
def url():
    # url = 'http://bms-3.yzwill.cn/'
    url = 'http://bms.yzwill.cn/'
    return url

def urls():
    # urls = "https://test.yzwill.cn/"
    urls = "http://zm-3.yzwill.cn/"
    return urls

def path_log():
    pwd = os.getcwd()
    p1 = os.path.dirname(os.path.abspath('.'))
    p2 = "test_reprot\log"
    path = os.path.join(pwd, p2)
    return path

def path_xlexcel():
    pwd = os.getcwd()
    p1 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    # Linxu系统
    #p2 = "test_data/Excel_File/ApiStudentBaseInfo.xlsx"
    # windows
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
    # Linxu系统
    #p2 = "test_report/report"
    # windows
    p2 = "test_report\\report"
    path = os.path.join(pwd, p2)
    return path


def path_jpg():
    pwd = os.getcwd()
    p1 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    # Linxu系统
    #p2 = "test_data/jpg/1.jpg"
    #windows
    p2 = "test_data\\jpg\\1.jpg"
    #调试用
    # path = os.path.join(p1, p2)
    #正式用
    path = os.path.join(pwd, p2)
    return path

def get_Invitation_url():
    '''邀约链接'''
    url = "http://zm-3.yzwill.cn/invite?action=login&inviteId=74c%2BQfTz20Ckbk8BiyTPt%2BrrtJMpWANS"
    return url

def loginUser():
    username = '蓝明勇'
    password = 'Yz123456'
    return username,password

def getEmailSender():
    sender = "lanmingyong@126.com"
    pwd = "mike5788973"

    return sender,pwd

def getEmailReceiver():
    receiver = "975922642@qq.com"

    return receiver