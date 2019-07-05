# import random
# # cj_enrolment = (50+66+78+99)
# # gk_enrolment = (12+55+6+0)
# # cj_pay = (50+40+30+0)
# # gk_pay = (12+11+3+0)
# # cj_drop_out = (2+0+1+0)
# # gk_drop_out = (1+1+2+0)
# # #个人成教缴费累计
# # # count=((cj_pay-cj_drop_out)*0.87+(gk_pay-gk_drop_out)*0.92)-8
# # count=(cj_pay)
# # print("个人成教缴费累计:%s" %count)
# # #个人成教只报名
# # count1=(cj_enrolment-cj_pay)
# # print("个人成教只报名:%s" %count1)
# # #个人国开报读累计标准人数
# # gkcount = gk_pay
# # print("个人国开报读累计标准人数:%s" %gkcount)
# # #预估标准人数
# # print("预估标准人数:%s" %(count*0.87+count1*0.09+gkcount*0.92-8))
# # #个人绩效(预估)
# # w=(count*0.87+count1*0.09+gkcount*0.92-8)*1000
# # print("个人绩效(预估):%s" %((count*0.87+count1*0.09+gkcount*0.92-8)*800))
# #
# #
# # print("叶仪炯主管总预估人数：%s" %(118.62+1495.76))
# # print("叶仪炯主管团队成教缴费总标准人数：%s" %(100+786+120))
# # print("叶仪炯主管团队成教只报名总标准人数：%s" %(10+534+173))
# # print("叶仪炯主管团队国开缴费总标准人数：%s" %(41+839+26))
# #
# #
# # print("杨立成校监总预估人数：%s" %(334.03))
# # print("杨立成校监团队成教缴费总标准人数：%s" %(197+786+100+120+14))
# # print("杨立成校监团队成教只报名总标准人数：%s" %(148+534+10+173+9))
# # print("杨立成校监团队国开缴费总标准人数：%s" %(171+839+41+26+3))
# #
# # print("杨立成校监团队梯度值：%s" %(320))
# # print("杨立成校监团队总标准任务数：%s" %(8+7+8+8+5))
# # print("杨立成校监团队总预估标准人数：%s" %((197+786+100+120+14)*0.87+(148+534+10+173+9)*0.09+(171+839+41+26+3)*0.92-36))
# # print("杨立成校监团队绩效为：%s" %(((197+786+100+120+14)*0.87+(148+534+10+173+9)*0.09+(171+839+41+26+3)*0.92-36)*320))
# #
# #
# #
# # print("戴吟绮助理成教缴费总标准人数：%s" %(14))
# # print("戴吟绮助理成教只报名总标准人数：%s" %(9))
# # print("戴吟绮助理国开缴费总标准人数：%s" %(3))
# # print("戴吟绮助理总预估人数：%s" %(14*0.87+9*0.09+3*0.92-5))
# # print("戴吟绮助理单生绩效值：%s" %(500))
# # print("戴吟绮助理个人绩效：%s" %((14*0.87+9*0.09+3*0.92-5)*500))
# #
# #
# # print("助学老师成教缴费总标准人数：%s" %(150))
# # print("助学老师成教只报名总标准人数：%s" %(150))
# # print("助学老师国开缴费总标准人数：%s" %(230))
# # print("助学老师总预估人数：%s" %(150*0.87+150*0.09+230*0.92-8))
# # print("助学老师单生绩效值：%s" %(1500))
# # print("助学老师个人绩效：%s" %((150*0.87+150*0.09+230*0.92-8)*1500))
# #
# #
# # #线上数据
# # print("陈春丽老师成教缴费总标准人数：%s" %(76))
# # print("陈春丽老师成教只报名总标准人数：%s" %(104-76))
# # print("陈春丽老师国开缴费总标准人数：%s" %(50))
# # print("陈春丽老师总预估人数：%s" %(76*0.87+28*0.09+50*0.92-8))
# # print("陈春丽老师单生绩效值：%s" %(850))
# # print("陈春丽老师个人绩效：%s" %((76*0.87+28*0.09+50*0.92-8)*850))
# # print("陈春丽老师预计个人年终绩效：%s" %((76*0.87+28*0.09+50*0.92-8)*850-4995))
# #
# # print("李兴老师成教缴费总标准人数：%s" %(87))
# # print("李兴老师成教只报名总标准人数：%s" %(7))
# # print("李兴老师国开缴费总标准人数：%s" %(102))
# # print("李兴老师总预估人数：%s" %(87*0.87+7*0.09+102*0.92-8))
# # print("李兴老师单生绩效值：%s" %(500))
# # print("李兴老师个人绩效：%s" %((87*0.87+7*0.09+102*0.92-8)*500))
# # print("李兴老师预计个人年终绩效：%s" %((87*0.87+7*0.09+102*0.92-8)*500-32506.31))
# #
# #
# # print("骆菁菁老师成教缴费总标准人数：%s" %(82))
# # print("骆菁菁老师成教只报名总标准人数：%s" %(9))
# # print("骆菁菁老师国开缴费总标准人数：%s" %(64))
# # print("骆菁菁老师总预估人数：%s" %(82*0.87+9*0.09+64*0.92-8))
# # print("骆菁菁老师单生绩效值：%s" %(850))
# # print("骆菁菁老师个人绩效：%s" %((82*0.87+9*0.09+64*0.92-8)*850))
# # print("骆菁菁老师预计个人年终绩效：%s" %(((82*0.87+9*0.09+64*0.92-8)*850)-6000))
# #
# # print("王荣寿老师成教缴费总标准人数：%s" %(80))
# # print("王荣寿老师成教只报名总标准人数：%s" %(38))
# # print("王荣寿老师国开缴费总标准人数：%s" %(59))
# # print("王荣寿老师总预估人数：%s" %(80*0.87+38*0.09+59*0.92-3))
# # print("王荣寿老师单生绩效值：%s" %(850))
# # print("王荣寿老师个人绩效：%s" %((80*0.87+38*0.09+59*0.92-3)*850))
# # print("王荣寿老师预计个人年终绩效：%s" %(((80*0.87+38*0.09+59*0.92-3)*850)-0))
# #
# # print("王荣寿老师团队成教缴费总标准人数：%s" %(160))
# # print("王荣寿老师团队成教只报名总标准人数：%s" %(54))
# # print("王荣寿老师团队国开缴费总标准人数：%s" %(114))
# # print("王荣寿老师团队总预估人数：%s" %(160*0.87+54*0.09+114*0.92-12))
# # print("王荣寿老师团队单生绩效值：%s" %(850))
# # print("王荣寿老师团队绩效：%s" %((80*0.87+38*0.09+59*0.92-12)*850))
# # print("王荣寿老师团队年终绩效：%s" %(((80*0.87+38*0.09+59*0.92-12)*850)-0))
# #
# # num=[1,3,6]
# # j= map(lambda x:x,num)
# # print(j)
# # newNumbers=tuple(map(lambda x:x,num))
# # print(newNumbers)

import time
# import base64
# import json
# params = {'mobile': '15632585787', 'valicode': '888888', 'notPrompt': '1', 'token': '', 'regChannel': '3',
#           'registerUrl': 'https://test.yzwill.cn?action=login&scholarship=&inviteId=&regOrigin=',
#           'bindType': '1', 'inviteToken': '', 'scholarship': '', 'idCard': '', 'regOrigin': '', 'channelId': '',
#           'sign': '', 'timeStamp': 'timeStamp'}
#
# r=bytes('{}'.format(params),'utf-8')
# params1 = base64.b64encode(r).decode('utf-8')
# print(params1)

# def neww(type,*s):
#     if type == True:
#         i = s[0]
#         j = s[1]
#         print(i,j)
#     else:
#         i = "ssss"
#         print(i)
#
# neww(1,'8888','sfdgg')

# from test_case.test_01_recruitAdd import *
#
#
# def addtestdata():
#     RecruitAddTest().test_00_login()
#     for i in range(0,10):
#         RecruitAddTest().test_01_cj_recruit_webtoken()
#         RecruitAddTest().test_02_cj_recruit()
#         # RecruitAddTest().test_03_gk_recruit_webtoken()
#         # RecruitAddTest().test_04_gk_recruit()
#
# addtestdata()
# #
# # for i in range(0,4):
# #     RecruitAddTest().test_00_login()
# #     RecruitAddTest().test_03_gk_recruit_webtoken()
# #     RecruitAddTest().test_04_gk_recruit()
class people():
    name=''
    age=0
    _weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print ("我的名字是："+str(self.name)+"我的年龄是："+str(self.age)+"我的体重是："+str(self._weight)+"kg")

class student(people):
    def xxx(self):
        self.speak()

student("小7",2,30).xxx()