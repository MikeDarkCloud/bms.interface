from myunit import *
from BmsApi import *
class OkConfirm(StartEnd):
    # @unittest.skip('skip this  case')
    def test_00_cj_okConfirm(self):
        '''测试成教学员考前确认'''
        response = BmsApi().okConfirm()
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员信息修改身份证失败！")
        self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员新生信息修改接口服务处理异常！！")


if __name__ == '__main__':
    unittest.main()