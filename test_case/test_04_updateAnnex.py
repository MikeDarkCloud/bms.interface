from model.myunit import *
from api.BmsApi import *
class UpdateAnnex(StartEnd):

    # @unittest.skip('skip this  case')
    def test_00_SFZZZ_upload(self):
        '''测试上传身份证正面图片'''
        response = BmsApi().updateAnnex(0)
        status_code = response[0]
        # code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员信息修改身份证失败！")
        # self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员新生信息修改接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_01_SFZZB_upload(self):
        '''测试上传身份证背面图片'''
        response = BmsApi().updateAnnex(1)
        status_code = response[0]
        # code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员信息修改身份证失败！")
        # self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员新生信息修改接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_02_XLZM_upload(self):
        '''测试上传学历图片'''
        response = BmsApi().updateAnnex(2)
        status_code = response[0]
        # code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员信息修改身份证失败！")
        # self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员新生信息修改接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_03_ZJZP_upload(self):
        '''测试上传证件相片图片'''
        response = BmsApi().updateAnnex(3)
        status_code = response[0]
        # code_text = response[1]
        self.assertEqual(status_code, 200, msg="学员信息修改身份证失败！")
        # self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教学员新生信息修改接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_04_SFZZZ_check(self):
        '''测试考前资料身份证正面图片核查'''
        response = BmsApi().charge(0)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="考前资料身份证正面图片核查失败！")
        self.assertEqual(code_text,'{"code":"00","body":null,"msg":"","ok":true}', msg="考前资料身份证正面图片核查接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_05_SFZZB_check(self):
        '''测试考前资料身份证背面图片核查'''
        response = BmsApi().charge(1)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="考前资料身份证背面图片核查失败！")
        self.assertEqual(code_text,'{"code":"00","body":null,"msg":"","ok":true}', msg="考前资料身份证背面图片核查接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_06_XLZM_check(self):
        '''测试上传学历图片核查'''
        response = BmsApi().charge(2)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="考前资料学历图片核查失败！")
        self.assertEqual(code_text,'{"code":"00","body":null,"msg":"","ok":true}', msg="考前资料上传学历图片核查接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_07_ZJZP_check(self):
        '''测试证件照片核查'''
        response = BmsApi().charge(3)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="考前资料证件照片核查失败！")
        self.assertEqual(code_text,'{"code":"00","body":null,"msg":"","ok":true}', msg="考前资料证件照片核查接口服务处理异常！！")

    # @unittest.skip('skip this  case')
    def test_08_annexCheck(self):
        '''测试考前资料最终核查'''
        response = BmsApi().check(1)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code, 200, msg="考前资料最终核查失败！")
        # self.assertEqual(code_text,'{"code":"00","body":null,"msg":"","ok":true}', msg="考前资料最终审核接口服务处理异常！！")


if __name__ == '__main__':
    unittest.main()