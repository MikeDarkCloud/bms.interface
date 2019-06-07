from myunit import *
from BmsApi import *
class Pay(StartEnd):
    # @unittest.skip('skip this  case')
    def test_01_cj_pay_webtoken(self):
        '''辅导费支付页面web_token获取'''
        self.assertEqual(BmsApi().toPay(1),200,msg="成教支付页面获取失败！")

    # @unittest.skip('skip this  case')
    def test_02_cj_pay(self):
        '''缴纳辅导费接口'''
        response = BmsApi().pay(1)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code,200,msg="成教辅导费支付失败")
        self.assertEqual(code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教辅导费支付接口服务处理失败！")

    # @unittest.skip('skip this  case')
    def test_03_cj_pay_check(self):
        '''辅导费缴费审核'''
        response = BmsApi().reviewFee(1)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code,200,msg="成教辅导费支付审核失败")
        self.assertEqual(code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成教辅导费支付审核接口服务处理失败！")

    # @unittest.skip('skip this  case')
    def test_04_gk_pay_webtoken(self):
        '''国开第一学期支付页面web_token获取'''
        self.assertEqual(BmsApi().toPay(2),200,msg="国开支付页面获取失败！")

    # @unittest.skip('skip this  case')
    def test_05_gk_pay(self):
        '''国开第一学期学费支付接口'''
        response = BmsApi().pay(2)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code,200,msg="国开支付接口调用失败！")
        self.assertEqual(code_text,'{"code":"00","body":"SUCCESS","msg":"","ok":true}',msg="国开支付接口服务处理失败！")

    # @unittest.skip('skip this  case')
    def test_06_gk_pay_check(self):
        '''国开第一学期缴费审核'''
        response = BmsApi().reviewFee(2)
        status_code = response[0]
        code_text = response[1]
        self.assertEqual(status_code,200,msg="国开第一学期支付审核失败")
        self.assertEqual(code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="成国开第一学期支付审核接口服务处理失败！")

if __name__ == '__main__':
    unittest.main()