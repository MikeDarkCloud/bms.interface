from GetTestData import *
import time
import base64
import logging
from time import sleep
import json
from GetUsTestData import *
class UsApi(rewrxl):

    def us_register(self):
        '''公众号注册接口'''
        endpoint = 'proxy/us/login/1.0/'
        urls = ''.join([Config.urls(),endpoint])
        data=GetUsTestData().get_us_login_data()
        r = requests.post(urls,headers=data[0], data=data[1],verify=False)
        pattern = re.compile(r'"auth_token":"(.+?)","relation"')
        auth_token = re.findall(pattern, r.text, flags=0)
        self.swrite_xl('Cookies','D', auth_token[0])
        print(r.text)
        return r.status_code,r.text

    def us_updateUserNam(self):
        '''公众号更新用户姓名接口'''
        endpoint = 'proxy/us/updateUserName/1.0/'
        urls = ''.join([Config.urls(),endpoint])
        data=GetUsTestData().get_us_updateUserName_data()
        r = requests.post(urls,headers=data[0], data=data[1],verify=False)
        print(r.text)
        # t= '{"body":"success","code":"00","message":"success","ok":true}'
        return r.status_code, r.text

    def us_sign(self):
        '''公众号更新用户姓名接口'''
        endpoint = 'proxy/us/sign/1.0/'
        urls = ''.join([Config.urls(),endpoint])
        data=GetUsTestData().get_us_sign_data()
        r = requests.post(urls,headers=data[0], data=data[1],verify=False)
        print(r.text)
        # t= '{"body":"5","code":"00","message":"success","ok":true}'
        return r.status_code, r.text

    def us_proxy_getCommitToken(self):
        '''获取报名zmtoken'''
        endpoint = 'proxy/proxy/getCommitToken/1.0/'
        urls = ''.join([Config.urls(),endpoint])
        data=GetUsTestData().get_proxy_getCommitToken_data()
        r = requests.post(urls,headers=data[0], data=data[1],verify=False)
        print(r.text)
        pattern = re.compile(r'"body":"(.+?)","code"')
        zmtoken = re.findall(pattern, r.text, flags=0)
        self.swrite_xl('UCJdata', 'N', zmtoken[0])
        # t= '{"body":"5","code":"00","message":"success","ok":true}'
        return r.status_code, r.text

    def us_cj_mkt_enroll(self):
        '''公众号成教报读接口'''
        endpoint = 'proxy/mkt/enroll/1.0/'
        urls = ''.join([Config.urls(),endpoint])
        data=GetUsTestData().get_cj_mkt_enroll_data()
        r = requests.post(urls,headers=data[0], data=data[1],verify=False)
        print(r.text)
        return r.status_code, r.text

    def us_gk_mkt_enroll(self):
        '''公众号国开报读接口'''
        endpoint = 'proxy/mkt/enroll/1.0/'
        urls = ''.join([Config.urls(),endpoint])
        data=GetUsTestData().get_gk_mkt_enroll_data()
        r = requests.post(urls,headers=data[0], data=data[1],verify=False)
        print(r.text)
        return r.status_code, r.text

if __name__ == '__main__':
    UsApi().us_register()
    UsApi().us_updateUserNam()
    UsApi().us_sign()
    UsApi().us_proxy_getCommitToken()
    UsApi().us_cj_mkt_enroll()
