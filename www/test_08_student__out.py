from myunit import *
from BmsApi import *
class StudentOut(StartEnd):

    # @unittest.skip('skip this  case')
    def test_00_cj_studentchange_getTestdata(self):
        '''测试成教转报测试数据在线生成'''
        try:
            BmsApi().toRecruitAdd(1)
            BmsApi().recruitAdd(1)
            BmsApi().toPay(1)
            BmsApi().pay(1)
            BmsApi().reviewFee(1)
            status_code = 'Success'
        except Exception as e:
            status_code = 'False'
        self.assertEqual(status_code, 'Success', msg="成教转报测试数据在线生成失败！")

    # @unittest.skip('skip this  case')
    def test_01_cj_studentOut_applyOut_webtoken(self):
        '''测试成教退学页面web_token获取'''
        response = BmsApi().studentOut_applyOut_webtoken()
        status_code = response
        self.assertEqual(status_code, 200, msg="成教学员转报页面web_token失败！")

    # @unittest.skip('skip this  case')
    def test_02_cj_student_out(self):
        '''测试成教学员退学申请接口'''
        response = BmsApi().addStudentOut()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="成教学员退学申请失败！")
        self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员退学申请接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_03_cj_studentOutApproval_editToFinancial_webtoken(self):
        '''测试成教学员退学审批页面web_token获取'''
        response = BmsApi().studentOutApproval_editToFinancial_webtoken()
        status_code = response
        self.assertEqual(status_code, 200, msg="成教学员转报页面web_token失败！")

    # @unittest.skip('skip this  case')
    def test_04_cj_passFinancialApproval(self):
        '''测试成教学员退学初次审批'''
        response = BmsApi().passFinancialApproval()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="成教学员退学申请失败！")
        self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员退学申请接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_05_cj_studentOutApproval_editToSchoolManaged_webtoken(self):
        '''测试成教学员退学审批页面web_token获取'''
        response = BmsApi().studentOutApproval_editToSchoolManaged_webtoken()
        status_code = response
        self.assertEqual(status_code, 200, msg="成教学员转报页面web_token失败！")

    # @unittest.skip('skip this  case')
    def test_06_cj_passSchoolManagedApproval(self):
        '''测试成教学员退学终审批'''
        response = BmsApi().passSchoolManagedApproval()
        status_code = response[0]
        code_text = response[1]
        cash = response[2]
        self.assertEqual(status_code, 200, msg="成教学员退学申请失败！")
        self.assertEqual(cash, '100', msg="成教学员退学申请失败！")
        self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员退学申请接口服务处理异常！！")


if __name__ == '__main__':
    unittest.main()