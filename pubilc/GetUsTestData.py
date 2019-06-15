import json
from XLExcel import *
import re
import json
from base import *
from Config import *
from CreateMobile import *
from CreateIdentity import *
from XLExcel import *
from ConnectMysql import *
from GetTestData import *
import time
import base64
import logging
from myunit import *
import urllib.parse
class GetUsTestData(rewrxl):
    '''接口参数组装类'''
    def get_us_login_data(self):
        '''组装公众号注册接口参数'''
        timeStamp=int(time.time())
        headers = {"Content-Type":"text/yzedu+;charset=utf-8","Accept": "application/json, text/plain, */*"}
        data={"header":{"appType":"2","frontTrace":""},"body":{"valicode":"888888","notPrompt":1,"token":"","regChannel":3,
                        "registerUrl":"http://zm-3.yzwill.cn?action=login&scholarship=&inviteId=&regOrigin=","bindType":"1","inviteToken":"",
                        "scholarship":"","idCard":"","regOrigin":"","channelId":"","sign":"","timeStamp":timeStamp}}
        mobile = create_mobile()
        self.swrite_xl('UCJdata','A', mobile)
        self.write_xl('C', mobile)
        data["body"]["mobile"]=mobile
        r = bytes('{}'.format(data), 'utf-8')
        logging.captureWarnings(True)
        datas = base64.b64encode(r).decode('utf-8')
        return headers,datas

    def get_us_updateUserName_data(self):
        '''组装更新用户姓名信息接口参数'''
        timeStamp = int(time.time())
        num = self.sread_xl('StudentNum', 'A')
        stdName = 'apiTest%s' %num
        self.swrite_xl('StudentNum','A',(num + 1))
        self.write_xl('A', stdName)
        self.swrite_xl('UCJdata','B', stdName)
        authtoken = self.sread_xl('Cookies', 'D')
        headers = {"Content-Type": "text/yzedu+;charset=utf-8", "Accept": "application/json, text/plain, */*","authtoken": authtoken}
        data = {"header": {"appType": "2", "frontTrace": ""},
                "body": {"realName": stdName, "sign": "", "timeStamp": timeStamp}}
        r = bytes('{}'.format(data), 'utf-8')
        logging.captureWarnings(True)
        datas = base64.b64encode(r).decode('utf-8')
        return headers,datas


    def get_us_sign_data(self):
        '''组装更新用户姓名信息接口参数'''
        authtoken = self.sread_xl('Cookies', 'D')
        timeStamp = int(time.time())
        headers = {"Content-Type": "text/yzedu+;charset=utf-8", "Accept": "application/json, text/plain, */*","authtoken": authtoken}
        data = {"header":{"appType":"2","frontTrace":""},"body":{"sign":"","timeStamp":timeStamp}}
        r = bytes('{}'.format(data), 'utf-8')
        logging.captureWarnings(True)
        datas = base64.b64encode(r).decode('utf-8')
        return headers,datas

    def get_proxy_getCommitToken_data(self):
        '''组装更新用户姓名信息接口参数'''
        authtoken = self.sread_xl('Cookies', 'D')
        timeStamp = int(time.time())
        headers = {"Content-Type": "text/yzedu+;charset=utf-8", "Accept": "application/json, text/plain, */*","authtoken": authtoken}
        data = {"header":{"appType":"2","frontTrace":""},"body":{"itName":"enroll","sign":"","timeStamp":timeStamp}}
        r = bytes('{}'.format(data), 'utf-8')
        logging.captureWarnings(True)
        datas = base64.b64encode(r).decode('utf-8')
        return headers,datas


    def get_cj_mkt_enroll_data(self):
        '''组装更新用户姓名信息接口参数'''
        authtoken = self.sread_xl('Cookies', 'D')
        timeStamp = int(time.time())
        scholarship= 36
        name = self.sread_xl('UCJdata','B')
        idCard = create_identity(int(area_dict1), 22, 1)
        self.swrite_xl('UCJdata','C', idCard)
        self.write_xl('A', idCard)
        grade  = 2020
        pfsnLevel = 5
        unvsId = 35
        unvsName = "华南农业大学"
        pfsnId = 25731580882379146
        pfsnName = "工商企业管理"
        taId = 164
        taName = "广州天河"
        zmtoken = self.sread_xl('UCJdata','N')
        headers = {"Content-Type": "text/yzedu+;charset=utf-8", "Accept": "application/json, text/plain, */*","authtoken": authtoken}
        data = {"header":{"appType":"2","frontTrace":""},
                "body":{"scholarship":scholarship,"name":name,"idCard":idCard,"recruitType":"1","grade":grade,"pfsnLevel":pfsnLevel,
                        "unvsId":unvsId,"unvsName":unvsName,"pfsnId":pfsnId,"pfsnName":pfsnName,"taId":taId,
                        "taName":taName,"zmtoken":zmtoken,"sg":"6","sign":"","timeStamp":timeStamp}}
        r = bytes('{}'.format(data), 'utf-8')
        logging.captureWarnings(True)
        datas = base64.b64encode(r).decode('utf-8')

        return headers,datas


    def get_gk_mkt_enroll_data(self):
        '''组装更新用户姓名信息接口参数'''
        authtoken = self.sread_xl('Cookies', 'D')
        timeStamp = int(time.time())
        scholarship= 1
        name = self.sread_xl('UCJdata','B')
        idCard = create_identity(int(area_dict1), 22, 1)
        self.swrite_xl('UCJdata','C', idCard)
        self.write_xl('A', idCard)
        grade  = 201909
        pfsnLevel = 5
        unvsId = 46
        unvsName = "国家开放大学"
        pfsnId = 155914292404924347
        pfsnName = "（12580）航天"
        taId = 164
        taName = "广州天河"
        zmtoken = self.sread_xl('UCJdata','N')
        headers = {"Content-Type": "text/yzedu+;charset=utf-8", "Accept": "application/json, text/plain, */*","authtoken": authtoken}
        data = {"header":{"appType":"2","frontTrace":""},"body":{"scholarship":scholarship,"name":name,"idCard":idCard,"recruitType":"2","grade":grade,
                                                                 "pfsnLevel":pfsnLevel,"unvsId":unvsId,"unvsName":unvsName,"pfsnId":pfsnId,"pfsnName":pfsnName,
                                                                 "taId":taId,"taName":taName,"zmtoken":zmtoken,"sg":"1","sign":"962E8F7E9C525D97B85FE941F0CE6E29","timeStamp":timeStamp}}
        r = bytes('{}'.format(data), 'utf-8')
        logging.captureWarnings(True)
        datas = base64.b64encode(r).decode('utf-8')

        return headers,datas