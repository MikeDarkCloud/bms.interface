from myunit import *
from BmsApi import *
class RecruitAddTest(StartEnd):
    def test_00_login(self):
        '''后台登录接口'''
        response = BmsApi().login()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="后台登录接口异常！")
        self.assertEqual(code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="后台登录接口异常！失败！")

    # @unittest.skip('skip this  case')
    def test_01_cj_recruit_webtoken(self):
        '''成教信息录入页面web_token获取'''
        self.assertEqual(BmsApi().toRecruitAdd(1), 200,msg="成教报读页面web_token获取成功！")

    # @unittest.skip('skip this  case')
    def test_02_cj_recruit(self):
        '''成教学员信息录入'''
        response = BmsApi().recruitAdd(1)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="成教学员报读接口调用失败！！")
        self.assertEqual(code_text, '{"code":"00","body":null,"msg":"","ok":true}', msg="成教学员报读接口服务处理失败！！")

    # @unittest.skip('skip this  case')
    def test_03_gk_recruit_webtoken(self):
        '''国开信息录入页面web_token获取'''
        self.assertEqual(BmsApi().toRecruitAdd(2), 200, msg="成教报读页面web_token获取成功！")

    # @unittest.skip('skip this  case')
    def test_04_gk_recruit(self):
        '''国开学员信息录入'''
        response = BmsApi().recruitAdd(2)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="国开学员报读接口调用失败！！")
        self.assertEqual(code_text, '{"code":"00","body":null,"msg":"","ok":true}', msg="国开学员报读接口服务处理失败！！")



if __name__ == '__main__':
    i = 5
    while i is True:
        RecruitAddTest().test_00_login()
        RecruitAddTest().test_01_cj_recruit_webtoken()
        RecruitAddTest().test_02_cj_recruit()
        i = i-1
