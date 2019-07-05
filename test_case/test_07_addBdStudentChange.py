from model.myunit import *
from api.BmsApi import *
class AddBdStudentChange(StartEnd):
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
    def test_01_cj_studentchange_webtoken(self):
        '''测试成教学员转报页面web_token获取'''
        response = BmsApi().studentChange_edit_webtoken(1)
        status_code = response
        self.assertEqual(status_code, 200, msg="成教学员转报页面web_token失败！")

    # @unittest.skip('skip this  case')
    def test_02_cj_studentchange(self):
        '''测试成教已缴199转报国开'''
        response = BmsApi().addBdStudentChange(1)
        status_code = response[0]
        code_text = response[1]
        coupon = response[2]
        self.assertEqual(coupon, 1, msg="成教学员转报国开未送199优惠券！")
        self.assertEqual(status_code, 200, msg="成教学员转报国开失败！")
        self.assertEqual(code_text,'{"code":"00","body":"success","msg":"","ok":true}', msg="成教学员转报国开接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_03_gk_studentchange_getTestdata(self):
        '''测试国开转报测试数据在线生成'''
        try:
            BmsApi().toRecruitAdd(2)
            BmsApi().recruitAdd(2)
            BmsApi().toPay(2)
            BmsApi().pay(2)
            BmsApi().reviewFee(2)
            status_code = 'Success'
        except Exception as e:
            status_code = 'False'
        self.assertEqual(status_code, 'Success', msg="国开转报测试数据在线生成失败！")

    # @unittest.skip('skip this  case')
    def test_04_gk_studentchange_webtoken(self):
        '''测试国开学员转报页面web_token获取'''
        response = BmsApi().studentChange_edit_webtoken(2)
        status_code = response
        self.assertEqual(status_code, 200, msg="国开学员转报页面web_token失败！")

    # @unittest.skip('skip this  case')
    def test_05_gk_studentchange(self):
        '''测试国开已缴第一学期费用转报成教'''
        response = BmsApi().addBdStudentChange(2)
        status_code = response[0]
        code_text = response[1]
        stranded_account = response[2]
        self.assertEqual(stranded_account, '1960', msg="国开已缴第一学期费用转报成教失败！")
        self.assertEqual(status_code, 200, msg="国开已缴第一学期费用转报成教失败！")
        self.assertEqual(code_text,'{"code":"00","body":"success","msg":"","ok":true}', msg="国开已缴第一学期费用转报成教接口服务处理异常！！")


if __name__ == '__main__':
    unittest.main()


