import requests
from GetTestData import *
from time import sleep
class BmsApi(rewrxl):
    '''bms接口'''
    def login(self):
        endpoint = 'login.do'
        user=Config().loginUser()
        urls = ''.join([Config().url(),endpoint])
        params = {"username": user[0], "password": user[1], "validCode": "1111"}
        r = requests.post(urls, params=params)
        print(r.status_code)
        print(r.text)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        print(cookies)
        self.swrite_xl('Cookies','B', str(cookies))
        return r.status_code,r.text

    def toRecruitAdd(self,recruitType):
        '''成教或国开报读页面接口调用获取web_token'''
        if recruitType == 1:
            endpoint = 'recruit/toRecruitAdd.do?rcruitType=%s' %recruitType
            urls = ''.join([Config().url(), endpoint])
            cookies = eval(self.sread_xl('Cookies','B'))
            r=requests.get(url=urls,cookies=cookies)
            # print(r.text)
            pattern = re.compile(r'(?<=(?:<input type="hidden" name="_web_token" value="))[1-9]\d*(?=(?:" />))')
            result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
            web_token = result[0]
            self.swrite_xl('Web_token','A', web_token)
            print(web_token)
            return r.status_code
        elif recruitType == 2:
            endpoint = 'recruit/toRecruitAdd.do?recruitType=%s' %recruitType
            urls = ''.join([Config().url(), endpoint])
            cookies = eval(self.sread_xl('Cookies','B'))
            r = requests.get(url=urls, cookies=cookies)
            pattern = re.compile(r'(?<=(?:<input type="hidden" name="_web_token" value="))[1-9]\d*(?=(?:" />))')
            result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
            web_token = result[0]
            self.swrite_xl('Web_token','D', web_token)
            print(web_token)
            return r.status_code
        else:
            print("别乱来，参数只能传1成教或2国开！")

    def recruitAdd(self,recruitType):
        '''成教或国开报读接口发起'''
        #获取组装好的参数
        if recruitType == 1:
            data=GetTestData().get_cj_toRecruitAdd_data()
            endpoint = 'recruit/recruitAdd.do'
            cookies = eval(self.sread_xl('Cookies','B'))
            urls = ''.join([Config().url(),endpoint])
            r = requests.post(urls,cookies=cookies,files=data)
            print(r.text)
            # self.assertEqual(r.status_code,200,msg='成教报读信息录入接口调用失败！')
            if r.status_code == 200:
                mobile=self.sread_xl('CJdata','B')
                mysql1 = "SELECT learn_id FROM bms.bd_learn_info WHERE mobile = '%s'" %mobile
                learn_Id_1 = ConnectMysql().select_mysql(mysql1)
                learn_Id = learn_Id_1[0][0]
                self.swrite_xl('CJdata','D', learn_Id)
                print(learn_Id)
                mysql1 = "SELECT std_id FROM bms.bd_student_info WHERE mobile = '%s'" % mobile
                std_id = ConnectMysql().select_mysql(mysql1)
                stdId = std_id[0][0]
                self.swrite_xl('CJdata','E', stdId)
                print(stdId)
                mysql2 = "SELECT sub_order_no FROM pay.bd_sub_order WHERE sub_learn_id = '%s' AND item_code = 'Y0'" %learn_Id
                orderNo=ConnectMysql().select_mysql(mysql2)
                orderNo = orderNo[0][0]
                self.swrite_xl('CJdata','F', orderNo)
                mysql2 = "SELECT annex_id FROM bms.bd_learn_annex WHERE learn_id = '%s' AND annex_type IN (1,2,3,5)" % learn_Id
                annex_id = ConnectMysql().select_mysql(mysql2)
                print(annex_id)
                self.swrite_xl('CJdata', 'H', annex_id[0][0])
                self.swrite_xl('CJdata', 'I', annex_id[1][0])
                self.swrite_xl('CJdata', 'J', annex_id[2][0])
                self.swrite_xl('CJdata', 'K', annex_id[3][0])
                mysql2 = "SELECT cr_id FROM bms.bd_check_record  WHERE mapping_id = %s  LIMIT 1" % learn_Id
                cr_id = ConnectMysql().select_mysql(mysql2)
                self.swrite_xl('CJdata', 'L', cr_id[0][0])
            else:
                print("成教学员报读接口异常请检查！！")
            return r.status_code,r.text
        elif recruitType == 2:
            '''国开报读接口发起'''
            # 获取组装好的参数
            data = GetTestData().get_gk_toRecruitAdd_data()
            endpoint = 'recruit/recruitAdd.do'
            cookies = eval(self.sread_xl('Cookies','B'))
            urls = ''.join([Config().url(), endpoint])
            # 发起调用
            r = requests.post(urls, cookies=cookies, files=data)
            print(r.text)
            # self.assertEqual(r.status_code, 200, msg='成教报读信息录入接口调用失败！')
            if r.status_code == 200:
                mobile = self.sread_xl('GKdata','B')
                mysql1 = "SELECT learn_id FROM bms.bd_learn_info WHERE mobile = '%s'" % mobile
                learn_Id_1 = ConnectMysql().select_mysql(mysql1)
                learn_Id = learn_Id_1[0][0]
                self.swrite_xl('GKdata','D', learn_Id)
                print(learn_Id)
                mysql1 = "SELECT std_id FROM bms.bd_student_info WHERE mobile = '%s'" % mobile
                std_id = ConnectMysql().select_mysql(mysql1)
                stdId = std_id[0][0]
                self.swrite_xl('GKdata','E', stdId)
                print(stdId)
                mysql2 = "SELECT sub_order_no  FROM pay.bd_sub_order WHERE sub_learn_id= '%s' and item_code in ('S1','W1','Y1')" % learn_Id
                orderNo = ConnectMysql().select_mysql(mysql2)
                print(orderNo)
                S1 = orderNo[0][0]
                W1 = orderNo[1][0]
                Y1 = orderNo[2][0]
                self.swrite_xl('GKdata','F', S1)
                self.swrite_xl('GKdata','G', W1)
                self.swrite_xl('GKdata','H', Y1)
            else:
                print("国开学员报读接口异常请检查！！")
            return r.status_code,r.text
        else:
            print("别乱来，参数只能传1成教或2国开！")

    def toPay(self,recruitType):
        '''支付页面web_token获取'''
        if recruitType == 1:
            learnId= self.sread_xl('CJdata','D')
            params = {'learnId':learnId}
            cookies = eval(self.sread_xl('Cookies','B'))
            endpoint = 'stdFee/toPay.do'
            r=requests.get(url=get_url(endpoint),params=params,cookies=cookies)
            pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
            result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
            web_token=result[0]
            self.swrite_xl('Web_token','B', web_token)
            return r.status_code
        elif recruitType == 2:
            learnId= self.sread_xl('GKdata','D')
            params = {'learnId':learnId}
            cookies = eval(self.sread_xl('Cookies','B'))
            endpoint = 'stdFee/toPay.do'
            r=requests.get(url=get_url(endpoint),params=params,cookies=cookies)
            pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
            result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
            web_token=result[0]
            self.swrite_xl('Web_token','E', web_token)
            return r.status_code
        else:
            print("你丫的，参数错了")

    def pay(self,recruitType):
        '''支付页面web_token获取'''
        endpoint1 = 'stdFee/pay.do'
        urls = ''.join([Config().url(), endpoint1])
        if recruitType == 1:
            data=GetTestData().get_cpay_data()
            cookies = eval(self.sread_xl('Cookies','B'))
            r = requests.post(urls, headers=data[0], cookies=cookies, data=data[1])
            print(r.status_code)
            print(r.text)
            return r.status_code,r.text
        elif recruitType == 2:
            data = GetTestData().get_gpay_data()
            cookies = eval(self.sread_xl('Cookies','B'))
            r = requests.post(urls, headers=data[0], cookies=cookies, data=data[1])
            print(r.status_code)
            print(r.text)
            return r.status_code,r.text
        else:
            print("你丫的，参数错了")
        # self.assertEqual((json.dumps(r_2.text,ensure_ascii=False))["code"], 00, msg='成教报读信息录入接口调用失败！')
        # self.assertEqual(r.status_code, 200, msg='成教报读信息录入接口调用失败！')

    def reviewFee(self,recruitType):
        '''缴费审核接口'''
        if recruitType == 1:
            endpoint1 = 'feeReview/reviewFee.do'
            urls = ''.join([Config().url(), endpoint1])
            data=GetTestData().get_cpay_review_data()
            cookies = eval(self.sread_xl('Cookies','B'))
            r = requests.post(urls, data=data, cookies=cookies)
            print(r.status_code)
            print(r.text)
            sleep(5)
            mysql2 = "SELECT zhimi_amount FROM us.us_base_info WHERE mobile = '%s'" % self.sread_xl('GKdata', 'B')
            zhimi_amount = ConnectMysql().select_mysql(mysql2)
            return r.status_code,r.text,zhimi_amount
        elif recruitType == 2:
            endpoint1 = 'feeReview/reviewFees.do'
            urls = ''.join([Config().url(), endpoint1])
            data=GetTestData().get_gpay_review_data()
            cookies = eval(self.sread_xl('Cookies','B'))
            r = requests.post(urls, data=data, cookies=cookies)
            print(r.status_code)
            print(r.text)
            return r.status_code,r.text
        else:
            print("坑爹，参数传错了，成教1国开2")



    def cj_studentModifyAdd(self,sheet,learnid,stdName):
        '''成教新生信息修改页面web_token获取'''
        cookies = eval(self.sread_xl('Cookies','B'))
        pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        r=requests.get(GetTestData().get_studentModifyAddWebToken_data(sheet,learnid,stdName), cookies=cookies)  #learn_id为C2 std_Name为H2
        #使用正则pattern为正则表达式，self.session.get(GetTestData().get_studentModifyAddWebToken_data).content.decode("utf-8")为请求返回数据并使用utf-8编码
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        print(result)
        web_token = result[0]
        self.swrite_xl('Web_token','C', web_token)
        return r.status_code

    def gk_studentModifyAdd(self,sheet,learnid,stdName):
        '''国开新生信息修改页面web_token获取'''
        cookies = eval(self.sread_xl('Cookies','B'))
        pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        r=requests.get(GetTestData().get_studentModifyAddWebToken_data(sheet,learnid,stdName), cookies=cookies)  #learn_id为C2 std_Name为H2
        #使用正则pattern为正则表达式，self.session.get(GetTestData().get_studentModifyAddWebToken_data).content.decode("utf-8")为请求返回数据并使用utf-8编码
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        print(result)
        web_token = result[0]
        self.swrite_xl('Web_token','F', web_token)
        return r.status_code,r.text

    def cj_insertStudentModify(self,newStdName,newIdCard,newSex,newUnvsId,newPfsnId):
        '''成教新生信息修改'''
        endpoint = 'studentModify/insertStudentModify.do'
        # 拼接url
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        #想修改什么就填什么
        r = requests.post(urls, data=GetTestData().get_cj_studentModifyAdd_data(newStdName,newIdCard,newSex,newUnvsId,newPfsnId),cookies=cookies)
        learn_Id = self.sread_xl('CJdata', 'D')
        mysql2 = "SELECT *FROM bms.bd_student_modify WHERE learn_id = '%s' ORDER BY create_time DESC LIMIT 1" % learn_Id
        modify_id = ConnectMysql().select_mysql(mysql2)
        print(modify_id[0][0])
        self.swrite_xl('CJdata', 'G', modify_id[0][0])
        return r.status_code,r.text

    def gk_insertStudentModify(self,newStdName,newIdCard,newSex,newUnvsId,newPfsnId):
        '''国开新生信息修改'''
        endpoint = 'studentModify/insertStudentModify.do'
        # 拼接url
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        #想修改什么就填什么
        r = requests.post(urls, data=GetTestData().get_gk_studentModifyAdd_data(newStdName,newIdCard,newSex,newUnvsId,newPfsnId),cookies=cookies)
        learn_Id = self.sread_xl('GKdata', 'D')
        mysql2 = "SELECT *FROM bms.bd_student_modify WHERE learn_id = '%s' ORDER BY create_time DESC LIMIT 1" % learn_Id
        modify_id = ConnectMysql().select_mysql(mysql2)
        print(modify_id[0][0])
        self.swrite_xl('GKdata', 'I', modify_id[0][0])
        return r.status_code,r.text

    def cj_editToAudit(self):
        '''成教新生信息修改审核页面web_token获取'''
        modifyId = self.sread_xl('CJdata', 'G')
        endpoint = 'studentModify/editToAudit.do?modifyId=%s&exType=UPDATE' %modifyId
        # 拼接url
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        #想修改什么就填什么
        pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        r = requests.get(urls,cookies=cookies)
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        web_token = result[0]
        self.swrite_xl('Web_token','G', web_token)
        return r.status_code,r.text

    def gk_editToAudit(self):
        '''成教新生信息修改审核页面web_token获取'''
        modifyId = self.sread_xl('GKdata', 'I')
        endpoint = 'studentModify/editToAudit.do?modifyId=%s&exType=UPDATE' %modifyId
        # 拼接url
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        r = requests.get(urls,cookies=cookies)
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        web_token = result[0]
        self.swrite_xl('Web_token','H', web_token)
        return r.status_code,r.text

    def passStudentAuditModify(self):
        '''新生信息修改审核'''
        endpoint = 'studentModify/passStudentAuditModify.do'
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        r = requests.post(urls,cookies=cookies,data=GetTestData().get_cj_passStudentAuditModify_data())
        return r.status_code, r.text

    def updateAnnex(self,num):
        '''附件上传'''
        endpoint = 'recruit/updateAnnex.do'
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        data = GetTestData().get_updateAnnex_data(num)
        r = requests.post(urls,cookies=cookies,files=data)
        return r.status_code, r.text

    def charge(self,num):
        '''考前资料核查接口'''
        endpoint = 'annexCheck/charge.do'
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        data = GetTestData().cj_charge_data(num)
        r = requests.post(urls,cookies=cookies,data=data)
        return r.status_code, r.text

    def check(self,recruitType):
        '''考前资料最终核查接口'''
        endpoint = 'annexCheck/check.do'
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        data = GetTestData().get_check_data(recruitType)
        r = requests.post(urls,cookies=cookies,data=data)
        return r.status_code, r.text

    def okConfirm(self):
        '''考前确认接口'''
        endpoint = 'testConfirm/okConfirm.do'
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        data = GetTestData().get_okConfirm_data()
        r = requests.post(urls,cookies=cookies,data=data)
        return r.status_code, r.text

    def studentScore_edit_webtoken(self):
        '''成考分数录入页面web_token获取'''
        endpoint = 'studentScore/edit.do?learnId=%s&idCard=%s&stdName=%s' %(self.sread_xl('CJdata', 'D'),self.sread_xl('CJdata', 'C'),self.sread_xl('CJdata', 'A'))
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        r = requests.post(urls,cookies=cookies)
        pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        web_token = result[0]
        self.swrite_xl('Web_token','I', web_token)
        return r.status_code

    def updateStudentScore(self):
        '''成考分数录入接口'''
        endpoint = 'studentScore/updateStudentScore.do'
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        r = requests.post(urls,cookies=cookies,data=GetTestData().get_updateStudentScore_data())
        return r.status_code, r.text

    def enroll(self):
        '''成教录取接口'''
        endpoint = 'stdEnroll/enroll.do'
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        r = requests.post(urls,cookies=cookies,data=GetTestData().get_enroll_data())
        return r.status_code, r.text


    def studentChange_edit_webtoken(self,recruitType):
        '''转报接口页面web_token获取'''
        if recruitType == 1:
            learnId=self.sread_xl('CJdata', 'D')
            stdName=self.sread_xl('CJdata', 'A')
            sheet = 'Web_token'
            cell='J'
            endpoint = 'studentChange/edit.do?exType=ADD&learnId=%s&stdName=%s' % (learnId, stdName)
            cookies = eval(self.sread_xl('Cookies', 'B'))
            urls = ''.join([Config().url(), endpoint])
            r = requests.get(urls, cookies=cookies)
            pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
            result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
            web_token = result[0]
            self.swrite_xl(sheet, cell, web_token)
            return r.status_code
        elif recruitType == 2:
            learnId=self.sread_xl('GKdata', 'D')
            stdName=self.sread_xl('GKdata', 'A')
            sheet = 'Web_token'
            cell='K'
            endpoint = 'studentChange/edit.do?exType=ADD&learnId=%s&stdName=%s' % (learnId, stdName)
            cookies = eval(self.sread_xl('Cookies', 'B'))
            urls = ''.join([Config().url(), endpoint])
            r = requests.get(urls, cookies=cookies)
            pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
            result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
            web_token = result[0]
            self.swrite_xl(sheet, cell, web_token)
            return r.status_code
        else:
            print("入参错误！！！")


    def addBdStudentChange(self,recruitType):
        '''转报接口'''
        if recruitType ==1:
            endpoint = 'studentChange/addBdStudentChange.do'
            cookies = eval(self.sread_xl('Cookies', 'B'))
            urls = ''.join([Config().url(), endpoint])
            r = requests.post(urls, cookies=cookies, data=GetTestData().get_addBdStudentChange_data(recruitType))
            mysql2 = "SELECT count(*) FROM bms.bd_student_coupon  WHERE std_id = '%s' and coupon_id = '1003'" % self.sread_xl('CJdata','E')
            coupon_count = ConnectMysql().select_mysql(mysql2)
            return r.status_code, r.text,coupon_count[0][0]
        elif recruitType ==2:
            endpoint = 'studentChange/addBdStudentChange.do'
            cookies = eval(self.sread_xl('Cookies', 'B'))
            urls = ''.join([Config().url(), endpoint])
            r = requests.post(urls, cookies=cookies, data=GetTestData().get_addBdStudentChange_data(recruitType))
            sleep(8)
            mysql2 = "SELECT stranded_account FROM bms.bd_student_info WHERE std_id = '%s'" % self.sread_xl('GKdata','E')
            stranded_account = ConnectMysql().select_mysql(mysql2)
            return r.status_code, r.text,stranded_account[0][0]

    def studentOut_applyOut_webtoken(self):
        '''成教学员退学页面web_token获取'''
        endpoint = 'studentOut/applyOut.do?learnId=%s&stdName=%s' %(self.sread_xl('CJdata', 'D'),self.sread_xl('CJdata', 'A'))
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        r = requests.get(urls,cookies=cookies)
        pattern = re.compile(r'(?<=(?:<input type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        web_token = result[0]
        self.swrite_xl('Web_token', 'L', web_token)

        return r.status_code

    def addStudentOut(self):
        '''退学申请发起接口'''
        endpoint = 'studentOut/addStudentOut.do'
        cookies = eval(self.sread_xl('Cookies', 'B'))
        urls = ''.join([Config().url(), endpoint])
        r = requests.post(urls, cookies=cookies, data=GetTestData().get_addStudentOut_data())
        mysql2 = "SELECT out_id FROM bms.bd_student_out WHERE std_id = '%s'" % self.sread_xl('CJdata', 'E')
        out_id = ConnectMysql().select_mysql(mysql2)
        self.swrite_xl('CJdata', 'M', out_id[0][0])
        return r.status_code, r.text

    def studentOutApproval_editToFinancial_webtoken(self):
        '''退学审批页面web_token获取接口'''
        reason = '成考未通过'
        endpoint = 'studentOutApproval/editToFinancial.do?outId=%s@2020@%s@%s@%s&exType=UPDATE&undo=false' %(self.sread_xl('CJdata', 'D'),self.sread_xl('CJdata', 'M'),self.sread_xl('CJdata', 'A'),urllib.parse.quote(reason))
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        r = requests.get(urls,cookies=cookies)
        pattern = re.compile(r'(?<=(?:type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        web_token = result[0]
        self.swrite_xl('Web_token','M', web_token)
        return r.status_code

    def passFinancialApproval(self):
        '''退学初审接口'''
        endpoint = 'studentOutApproval/passFinancialApproval.do'
        cookies = eval(self.sread_xl('Cookies', 'B'))
        urls = ''.join([Config().url(), endpoint])
        r = requests.post(urls, cookies=cookies, data=GetTestData().get_passFinancialApproval())
        return r.status_code, r.text

    def studentOutApproval_editToSchoolManaged_webtoken(self):
        '''退学终审页面web_token获取接口'''
        reason = '成考未通过'
        endpoint = 'studentOutApproval/editToSchoolManaged.do?outId=%s@2020@%s@%s@%s&exType=UPDATE&undo=false' %(self.sread_xl('CJdata', 'D'),self.sread_xl('CJdata', 'M'),self.sread_xl('CJdata', 'A'),urllib.parse.quote(reason))
        cookies = eval(self.sread_xl('Cookies','B'))
        urls = ''.join([Config().url(),endpoint])
        r = requests.get(urls,cookies=cookies)
        pattern = re.compile(r'(?<=(?:type="hidden" value="))[1-9]\d*(?=(?:" name="_web_token"))')
        result = re.findall(pattern, r.content.decode("utf-8"), flags=0)
        web_token = result[0]
        self.swrite_xl('Web_token','M', web_token)
        return r.status_code

    def passSchoolManagedApproval(self):
        '''退学终审接口'''
        endpoint = 'studentOutApproval/passSchoolManagedApproval.do'
        cookies = eval(self.sread_xl('Cookies', 'B'))
        urls = ''.join([Config().url(), endpoint])
        r = requests.post(urls, cookies=cookies, data=GetTestData().get_passSchoolManagedApproval())
        sleep(8)
        mysql2 = "SELECT cash_account FROM bms.bd_student_info WHERE std_id = '%s'" % self.sread_xl('CJdata', 'E')
        cash = ConnectMysql().select_mysql(mysql2)
        return r.status_code, r.text,cash[0][0]


if __name__ == '__main__':
    BmsApi().login()
    # BmsApi().toRecruitAdd(1)

