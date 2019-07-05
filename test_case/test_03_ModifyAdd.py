from model.myunit import *
from api.BmsApi import *
from pubilc.CreateIdentity import *
class StudentModifyAdd(StartEnd):

    # @unittest.skip('skip this  case')
    def test_01_cj_modify_webtoken(self):
        '''成教新生信息异动页面web_token获取'''
        self.assertEqual(BmsApi().cj_studentModifyAdd('CJdata','D','A'),200,msg="学员信息修改页面webtoken获取失败！")

    # @unittest.skip('skip this  case')
    def test_02_cj_modify_newidcard(self):
        '''成教学员新生信息异动申请'''
        response = BmsApi().cj_insertStudentModify('',create_identity(int(area_dict1), 22, 1),'','','')
        '''参数依次为newStdName,newIdCard,newSex,newUnvsId，newPfsnId'''
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员信息修改身份证失败！")
        self.assertEqual(code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员新生信息修改接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_03_cj_editToAudit(self):
        '''成教新生信息修改审核页面web_token获取'''
        response = BmsApi().cj_editToAudit()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员新生信息修改审核页面获取失败！")

    # @unittest.skip('skip this  case')
    def test_04_cj_passStudentAuditModify(self):
        '''成教新生信息修改审核接口'''
        response = BmsApi().passStudentAuditModify()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员新生信息修改审核失败！")
        self.assertEqual(code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="学员新生信息修改审核失败服务处理异常！！")


if __name__ == '__main__':
    unittest.main()