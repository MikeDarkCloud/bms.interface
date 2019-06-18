from myunit import *
from UsApi import *
class UsRegister(StartEnd):

    # @unittest.skip('skip this  case')
    def test_00_cj_us_register_success(self):
        '''测试公众号登录登录注册接口'''
        response = UsApi().us_register()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="公众号登录登录注册接口调用失败！")
        # self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员退学申请接口服务处理异常！！")

    def test_01_cj_us_updateUserNam_success(self):
        '''测试公众号更新会员姓名接口'''
        response = UsApi().us_updateUserNam()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="公众号更新用户姓名接口调用失败！")
        self.assertEqual(code_text,'{"body":"success","code":"00","message":"success","ok":true}', msg="公众号更新用户姓名接口调用失败！！")

    def test_02_cj_us_sign_success(self):
        '''测试公众号签到接口'''
        response = UsApi().us_sign()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="公众号签到接口调用失败！")
        self.assertEqual(code_text,'{"body":"5","code":"00","message":"success","ok":true}', msg="公众号签到接口异常！！")

    def test_03_cj_us_proxy_getCommitToken_success(self):
        '''测试获取报名zmtoken'''
        response = UsApi().us_proxy_getCommitToken()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="公众号获取报名zmtoken接口调用失败！")
        self.assertEqual(code_text,'{"body":"5","code":"00","message":"success","ok":true}', msg="公众号获取报名zmtoken接口异常！！")

    def test_04_cj_us_mkt_enroll(self):
        '''测试公众号报读成教院校'''
        UsApi().us_proxy_getCommitToken()
        response = UsApi().us_cj_mkt_enroll()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="公众号报读成教院校接口调用失败！")
        # self.assertEqual(code_text,'{"body":"5","code":"00","message":"success","ok":true}', msg="公众号获取报名zmtoken接口异常！！")

    def test_05_us_gk_mkt_enroll(self):
        '''测试公众号报读国开院校'''
        UsApi().us_proxy_getCommitToken()
        response = UsApi().us_gk_mkt_enroll()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="公众号报读国开院校接口调用失败！")
        # self.assertEqual(code_text,'{"body":"5","code":"00","message":"success","ok":true}', msg="公众号获取报名zmtoken接口异常！！")
