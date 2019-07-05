from model.myunit import *
from api.BmsApi import *
class updateStudentScore(StartEnd):
    # @unittest.skip('skip this  case')
    def test_00_cj_studentScore_edit(self):
        '''测试成教学员成考分数录入页面web_token获取'''
        response = BmsApi().studentScore_edit_webtoken()
        status_code = response
        self.assertEqual(status_code, 200, msg="成教学员成考分数录入页面web_token失败！")

    def test_01_cj_updateStudentScore(self):
        '''测试成教学员成考分数录入'''
        response = BmsApi().updateStudentScore()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="成教学员成考分数录入证失败！")
        self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员成考分数录入接口服务处理异常！！")

    def test_02_cj_stdEnroll_enroll(self):
        '''测试成教学员录取'''
        response = BmsApi().enroll()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="成教学员成考分数录入失败！")
        self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员成考分数录入接口服务处理异常！！")

    def test_studentChange_edit_webtoken(self):
        '''测试成教学员转报国开'''
        response = BmsApi().studentScore_edit_webtoken()
        status_code = response
        self.assertEqual(status_code, 200, msg="成教学员成考分数录入页面web_token失败！")



if __name__ == '__main__':
    unittest.main()