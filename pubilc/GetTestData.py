import json
import re
import json
from model.base import *
from model.Config import *
from pubilc.CreateMobile import *
from pubilc.CreateIdentity import *
from pubilc.XLExcel import *
from pubilc.ConnectMysql import *
from model.myunit import *
import urllib.parse
class GetTestData(rewrxl):
    '''接口参数组装类'''

    def get_gk_toRecruitAdd_data(self):
        data = {"adminssionTime":(None, ""),"birthday":(None, "1990-03-07"),"bpType":(None, 1),
                "diploma": (None, ""),"edcsSystem":(None, ""),"email":(None, ""),"emergencyContact":(None, ""),"enrollType":(None, 1),
                "graduateTime":(None, "2019-05-29"),"headPic":(None, ""),"headPortrait":(None, ""),"idType":(None, 1),
                "isOpenUnvs": (None, 0),"isPhotoChange":(None, ""),"jobStatus":(None, 1),"jobTitle":(None, ""),"maritalStatus":(None, 1),"materialCode":(None, ""),"materialType":(None, ""),
                "nation":(None, "01"),"nowCityCode":(None, 1601),"nowCityName":(None, "广州市"),"nowDistrictCode":(None, 3633),"nowDistrictName":(None, "天河区"),
                "nowProvinceCode": (None, 19),"nowProvinceName":(None, "广东"),"nowStreetCode":(None, ""),"nowStreetName":(None, "--请选择--"),"offerId":(None, ""),"oldCityCode":(None, ""),
                "oldProvinceCode": (None, ""),"pfsnLevel":(None, 5),"points":(None, 0),"politicalStatus":(None, "01"),"profession":(None, ""),
                "qq": (None, ""),"remark":(None, ""),"rprCityCode":(None, 440100),"rprDistrictCode":(None, 440103),"rprProvinceCode":(None, 440000),"rprType":(None, 1),
                "secUnvsId":(None, ""),"sex":(None, 1),"stdId":(None, ""),"studyType":(None, ""),"subject":(None, ""),"subjectCategory":(None, ""),"taId":(None, 155652772059540424),
                "telephone": (None, ""),"unvsName":(None, "社会大学"),"wechat":(None, ""),"workPlace":(None, ""),"wpAddress":(None, ""),"wpCityCode":(None, ""),
                "wpProvinceCode": (None, ""),"wpTelephone":(None, ""),"wpTime":(None, ""),"zipCode":(None, 510000),'address': (None, '猎德街冼村4号')}
        #bms-3
        num = self.sread_xl('StudentNum', 'A')
        stdName = 'apiTest%s' %num
        self.swrite_xl('StudentNum','A',(num + 1))
        self.write_xl('A', stdName)
        self.swrite_xl('GKdata','A', stdName)
        data['stdName'] = (None, stdName)
        web_token=self.sread_xl('Web_token','D')
        data['_web_token'] = (None, web_token)
        mobile = create_mobile()
        self.swrite_xl('GKdata','B', mobile)
        self.write_xl('C', mobile)
        data['mobile'] = (None, mobile)
        idCard = create_identity(int(area_dict1), 22, 1)
        self.swrite_xl('GKdata','C', idCard)
        self.write_xl('B', idCard)
        data['idCard'] = (None, idCard)
        data['scholarship'] = (None, 1)
        data['city'] = (None, 440100)
        data['grade'] = (None, 201909)
        data['feeId'] = (None, 155653679375736887)
        data['edcsType'] = (None, 1)
        data['pfsnId'] = (None, 155653111406054610)
        data['recruitType'] = (None, 2)
        data['unvsId'] = (None, 46)

        return data

    def get_cj_toRecruitAdd_data(self):
        '''组装成教报读报读信息学录入接口参数'''
        data = {'stdId': (None, ''), 'recruitType': (None, 1), 'nowProvinceName': (None, '广东'),
                'nowCityName': (None, '广州市'), 'nowDistrictName': (None, '天河区'), 'nowStreetName': (None, '--请选择--'),
                 'idType': (None, 1), 'sex': (None, 1), 'birthday': (None, '1994-03-07'),
                'nation': (None, '01'),
                'politicalStatus': (None, '01'), 'rprType': (None, 1), 'rprProvinceCode': (None, 430000),
                'rprCityCode': (None, 430100), 'rprDistrictCode': (None, 430102), 'rprAddressCode': (None, 440101),
                'nowProvinceCode': (None, 19), 'nowCityCode': (None, 1601), 'nowDistrictCode': (None, 3633),
                'nowStreetCode': (None, ''), 'address': (None, '猎德街冼村4号'), 'jobType': (None, 11), 'wpTime': (None, ''),
                'wpProvinceCode': (None, ''), 'wpCityCode': (None, ''), 'wpAddress': (None, ''),
                'wpTelephone': (None, ''), 'zipCode': (None, 100000), 'emergencyContact': (None, ''),
                'headPic': (None, ''), 'headPortrait': (None, ''),
                'isPhotoChange': (None, ''), 'telephone': (None, ''), 'email': (None, ''), 'qq': (None, ''),
                'wechat': (None, ''), 'jobTitle': (None, ''), 'workPlace': (None, ''), 'maritalStatus': (None, ''),
                'remark': (None, ''), 'edcsType': (None, 1),
                'unvsName': (None, '社会大学'), 'oldProvinceCode': (None, ''), 'oldCityCode': (None, ''),
                'adminssionTime': (None, ''), 'graduateTime': (None, '2019-05-20'), 'profession': (None, '汽车运用与维修'),
                'diploma': (None, 888888), 'edcsSystem': (None, ''), 'subject': (None, ''),
                'subjectCategory': (None, ''), 'studyType': (None, ''), 'materialType': (None, ''),
                'materialCode': (None, ''), 'pfsnLevel': (None, 5),
                'enrollType': (None, 1), 'grade': (None, 2020), 'unvsId': (None, 35),
                'pfsnId': (None, 25731580882379146), 'taId': (None, 161), 'secUnvsId': (None, ''), 'bpType': (None, 3),
                'points': (None, 20), 'feeId': (None, 156206015248035566), 'offerId': (None, '')}
        #bms-3 'feeId': (None, 155791403587912802)  'pfsnId': (None, 154805425064430654)
        num = self.sread_xl('StudentNum','A')
        stdName = 'apiTest%s' %num
        self.swrite_xl('StudentNum','A',(num + 1))
        self.write_xl('A', stdName)
        self.swrite_xl('CJdata','A', stdName)
        data['stdName'] = (None, stdName)
        web_token=self.sread_xl('Web_token','A')
        data['_web_token'] = (None, web_token)
        mobile = create_mobile()
        print(mobile)
        self.swrite_xl('CJdata','B', mobile)
        self.write_xl('C', mobile)
        data['mobile'] = (None, mobile)
        idCard = create_identity(int(area_dict1), 22, 1)
        self.swrite_xl('CJdata','C', idCard)
        self.write_xl('B', idCard)
        data['idCard'] = (None, idCard)
        data['scholarship'] = (None, 37)

        return data

    def get_cpay_data(self):
        '''成教辅导费后台支付接口参数组装'''
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {"grade": 2020, "years": 0,"itemCodes": "Y0", "accDeduction": 0.00, "couponsStr": [],
                 "zmDeduction": "0","payableCount": "199.00", "paymentType": 1, "remark": ""}
        payData={"paymentType": "1", "tradeType":"NATIVE",
                    "accDeduction": "0.00", "zmDeduction": 0, "coupons" :"[]",
                    "dataSources": "5", "grade": "2020", "payAmount":199.00,"remark": ""}

        data["_web_token"]=self.sread_xl('Web_token','B')
        learn_id = self.sread_xl('CJdata','D')
        data["learnId"]=learn_id
        payData["learnId"]=learn_id
        # items = "[{\"itemCode\":\"Y0\",\"itemName\":\"考前辅导费11\",\"itemYear\":\"0\",\"amount\":\"199.00\",\"accScale\":0,\"zmScale\":0,\"couponScale\":0,\"payAmount\":\"199.00\"}]"
        items1=[]
        items = {"itemCode":"Y0","itemName":"考前辅导费11","itemYear":"0","amount":"199.00","accScale":0,"zmScale":"0","couponScale":0,"payAmount":"199.00"}
        items["orderNo"] = self.sread_xl('CJdata','F')
        items1.append(items)
        payData["items"] =str(items1).replace('"','\\'+'\"')
        data["payData"]=json.dumps(payData,ensure_ascii=False)
        return headers,data

    def get_gpay_data(self):
        '''国开后台支付接口参数组装'''
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {"grade": 1909, "years": 1,"itemCodes": "S1", "itemCodes": "W1","itemCodes": "Y1","accDeduction": 0.00, "couponsStr": [],
                 "zmDeduction": "0","payableCount": "1960.00", "paymentType": 1, "remark": ""}
        payData={"paymentType": "1", "tradeType":"NATIVE",
                 "accDeduction": "0.00", "zmDeduction": "0", "coupons" :"[]",
                 "dataSources": "5", "grade": "1909", "payAmount":"1960.00","remark": ""}

        data["_web_token"]=self.sread_xl('Web_token','E')
        learn_id = self.sread_xl('GKdata','D')
        data["learnId"]=learn_id
        payData["learnId"]=learn_id
        items=[{"itemName":"代收第一年书费","accScale":0,"zmScale":0,"couponScale":0},
               {"itemName":"代收第一年网络费","accScale":0,"zmScale":0,"couponScale":0},
               {"itemName":"代收第一年学费","accScale":0,"zmScale":0,"couponScale":0}]
        items[0]["orderNo"] = self.sread_xl('GKdata','F')
        items[1]["orderNo"] = self.sread_xl('GKdata','G')
        items[2]["orderNo"] = self.sread_xl('GKdata','H')
        items[0]["itemCode"] = "S1"
        items[1]["itemCode"] = "W1"
        items[2]["itemCode"] = "Y1"
        items[0]["itemYear"] = "1"
        items[1]["itemYear"] = "1"
        items[2]["itemYear"] = "1"
        items[0]["amount"] = "250.00"
        items[1]["amount"] = "150.00"
        items[2]["amount"] = "1560.00"
        items[0]["payAmount"] = "250.00"
        items[1]["payAmount"] = "150.00"
        items[2]["payAmount"] = "1560.00"
        # items1.append(items)
        payData["items"] =str(items).replace('"','\\'+'\"')
        data["payData"]=json.dumps(payData,ensure_ascii=False)
        return headers,data



    def get_studentModifyAddWebToken_data(self,sheet,learnid,stdName):
        '''新生信息修改页面接口数据组装'''
        #成教sheet为CJdata learnid为D stdName为A  国开sheet为GKdata learn_id为D std_Name为A
        learnId = self.sread_xl(sheet,learnid)
        stdName = self.sread_xl(sheet,stdName)
        endpoint = 'studentModify/add.do?learnId=%s&stdName=%s&exType=ADD' %(learnId,urllib.parse.quote(stdName))
        host = Config().url()
        # 拼接url
        urls = ''.join([host,endpoint])
        return urls

    def get_cj_studentModifyAdd_data(self,newStdName,newIdCard,newSex,newUnvsId,newPfsnId):
        '''成教新生信息新修改接口数据组装'''
        data = { 'ifCanUpdate': 'true',
                   'nation': '01', 'newNation': '','taIdv': '广州荔湾', 'taId': 161,
                  'newTaId': 230, 'scholarship': 36, 'newScholarship': '', }
        data['_web_token'] = self.sread_xl('Web_token','C')
        data['grade'] = '2020'
        data['stdId'] = self.sread_xl('CJdata','E')
        data['stdName'] = self.sread_xl('CJdata','A')
        data['newStdName'] = '%s' %newStdName
        data['idCard'] = self.sread_xl('CJdata','C')
        data['newIdCard'] = '%s' %newIdCard
        data['pfsnId'] = 25731580882379146
        data['sex'] = '1'
        data['newSex'] = '%s' %newSex
        data['unvsId'] = 35
        data['newUnvsId'] = '%s' %newUnvsId
        data['pfsnLevel'] = 5
        data['newPfsnId'] = '%s' %newPfsnId
        data['learnId'] = self.sread_xl('CJdata','D')
        print(data)
        return data

    def get_gk_studentModifyAdd_data(self,newStdName,newIdCard,newSex,newUnvsId,newPfsnId):
        '''国开新生信息新修改接口数据组装'''
        data = { 'ifCanUpdate': 'true',
                   'nation': '01', 'newNation': '','taIdv': '广州荔湾', 'taId': 161,
                  'newTaId': 230, 'scholarship': 36, 'newScholarship': '', }
        data['_web_token'] = self.sread_xl('Web_token','F')
        data['grade'] = '2020'
        data['stdId'] = self.sread_xl('GKdata','E')
        data['stdName'] = self.sread_xl('GKdata','A')
        data['newStdName'] = '%s' %newStdName
        data['idCard'] = self.sread_xl('GKdata','C')
        data['newIdCard'] = '%s' %newIdCard
        data['pfsnId'] = 25731580882379146
        data['sex'] = '1'
        data['newSex'] = '%s' %newSex
        data['unvsId'] = 35
        data['newUnvsId'] = '%s' %newUnvsId
        data['pfsnLevel'] = 5
        data['newPfsnId'] = '%s' %newPfsnId
        data['learnId'] = self.sread_xl('GKdata','D')
        print(data)
        return data

    def get_cpay_review_data(self):
        '''成教支付审核接口数据组装'''
        data={}
        data["subOrderNo"] = self.sread_xl('CJdata','F')
        data["learnId"] = self.sread_xl('CJdata','D')
        return data


    def get_gpay_review_data(self):
        '''国开支付审核接口数据组装'''
        subOrderNos1=(self.sread_xl('GKdata','F'))
        subOrderNos2=(self.sread_xl('GKdata','G'))
        subOrderNos3=(self.sread_xl('GKdata','H'))
        learnId=(self.sread_xl('GKdata','D'))
        data = [{"subOrderNo": subOrderNos1, "learnId": learnId}, {"subOrderNo": subOrderNos2, "learnId": learnId},
                {"subOrderNo": subOrderNos3, "learnId": learnId}]
        return data

    def get_cj_passStudentAuditModify_data(self):
        '''成教新生信息修改审核接口数据组装'''
        data = {"exType":"UPDATE","crId":"","checkStatus":2,"reason":""}
        data["modifyId"]=self.sread_xl('CJdata','G')
        data["_web_token"]=self.sread_xl('Web_token','G')
        return data

    def get_gk_passStudentAuditModify_data(self):
        '''国开新生信息修改审核接口数据组装'''
        data = {"exType":"UPDATE","crId":"","checkStatus":2,"reason":""}
        data["modifyId"]=self.sread_xl('CJdata','I')
        data["_web_token"]=self.sread_xl('Web_token','H')
        return data

    def get_updateAnnex_data(self,num):
        '''成教附件上传接口数据组装'''
        learn_Id = self.sread_xl('CJdata', 'D')
        annexId0 = self.sread_xl('CJdata', 'H')
        annexId1 = self.sread_xl('CJdata', 'I')
        annexId2 = self.sread_xl('CJdata', 'J')
        annexId3 = self.sread_xl('CJdata', 'K')
        data = {"annexUrl": (None, ""),}
        data["annexFile"] = ("1.jpg", open(Config.path_jpg(), "rb"), "image/jpeg")
        data["learnId"] = (None, learn_Id)
        data["isRequire"] = (None, 1)
        if num ==0:
            data["annexId"] = (None,annexId0)
            data["annexName"] = (None, "身份证正面照")
            data["annexType"] = (None, 1)
        elif num ==1:
            data["annexId"] = (None,annexId1)
            data["annexName"] = (None, "身份证背面照")
            data["annexType"] = (None, 2)
        elif num == 2:
            data["annexId"] = (None,annexId2)
            data["annexName"] = (None, "学历证书")
            data["annexType"] = (None, 3)
        elif num == 3:
            data["annexId"] = (None,annexId3)
            data["annexName"] = (None, "相片")
            data["annexType"] = (None, 5)
        else:
            print("入参传错了！！！！")
        return data

    def cj_charge_data(self,num):
        '''考前资料核查接口参数组装'''
        data = {}
        learn_Id = self.sread_xl('CJdata', 'D')
        data["learnId"]=learn_Id
        data["annexStatus"]=3
        if num == 0:
            data["annexId"]= self.sread_xl('CJdata', 'H')
        elif num == 1:
            data["annexId"] = self.sread_xl('CJdata', 'I')
        elif num == 2:
            data["annexId"] = self.sread_xl('CJdata', 'J')
        elif num == 3:
            data["annexId"] = self.sread_xl('CJdata', 'K')
        else:
            print("入参错误！！")
        return data

    def get_check_data(self,recruitType):
        '''考前资料核查接口参数组装'''
        data={"isDataCheck":1,"jtId":"null"}
        data["recruitType"] =recruitType
        data["crId"] =self.sread_xl('CJdata', 'L')
        data["learnId"] =self.sread_xl('CJdata', 'D')
        return data

    def get_okConfirm_data(self):
        '''考前确认接口参数组装'''
        data = {"exType":"exType"}
        data["learnId"] = self.sread_xl('CJdata', 'D')
        return data

    def get_updateStudentScore_data(self):
        '''成考分数录入接口参数组装'''
        data = {}
        data["learnId"]=self.sread_xl('CJdata', 'D')
        data["_web_token"]=self.sread_xl('Web_token', 'I')
        # data["scores"] = [[{"courseId":"0009"},{"courseName":"数学"},{"score":"80"}],[{"courseId":"0010"},{"courseName":"语文"},{"score":"81"}],[{"courseId":"0014"},{"courseName":"专科外语"},{"score":"82"}]]
        data["scores[0].courseId"] = "0009"
        data["scores[0].courseName"] = "数学"
        data["scores[0].score"] = "80"
        data["scores[1].courseId"] = "0010"
        data["scores[1].courseName"] = "语文"
        data["scores[1].score"] = "81"
        data["scores[2].courseId"] = "0014"
        data["scores[2].courseName"] = "专科外语"
        data["scores[2].score"] = "83"
        return data

    def get_enroll_data(self):
        '''成教录入接口参数组装'''
        data = {}
        data["_web_token"]=""
        data["learnId"]=self.sread_xl('CJdata', 'D')
        data["grade"]=2020
        data["pfsnId"]=25731580882379146
        data["unvsId"]=35
        data["fenshu"]=244
        data["campusIds"]=""
        return data

    def get_addBdStudentChange_data(self,recruitType):
        '''成教学员转报接口参数组装'''
        if recruitType ==1:
            data={}
            data["_web_token"] = self.sread_xl('Web_token', 'J')
            data["stdId"] = self.sread_xl('CJdata', 'E')
            data["oldLearnId"] = self.sread_xl('CJdata', 'D')
            data["grade"] = 201909
            data["unvsId"] = 155351393833756653
            data["pfsnId"] = 155653092080007753
            data["taId"] = 155652772059540424
            data["scholarship"] = 1
            data["recruit"] = ""
            data["recruitDpId"] = ""
            data["recruitCampusId"] = ""
            data["recruitGroupId"] = ""
            data["recruitCampusManager"] = ""
            data["dpManager"] = ""
            data["exType"] = "ADD"
            data["ifCanUpdate"] = "true"
            data["isSuper"] = 1
            data["recruitType"] = ""
            data["learnId"] = ""
            data["stdName"] = ""
            data["oldStdStage"] = 2
            data["pfsnLevel"] = 5
            data["assignFlag"] = 0
            data["groupManager"] = ""
            data["reason"] = ""
            return data
        elif recruitType ==2:
            data={}
            data["_web_token"] = self.sread_xl('Web_token', 'K')
            data["stdId"] = self.sread_xl('GKdata', 'E')
            data["oldLearnId"] = self.sread_xl('GKdata', 'D')
            data["grade"] = 2020
            data["unvsId"] = 35
            data["pfsnId"] = 25731580882379146
            data["taId"] = 161
            data["scholarship"] = 36
            data["recruit"] = 153942319625374821
            data["recruitDpId"] = 154451004456475432
            data["recruitCampusId"] = 1754661637535500494
            data["recruitGroupId"] = ""
            data["recruitCampusManager"] = 429
            data["dpManager"] = 457743676860765859
            data["exType"] = "ADD"
            data["ifCanUpdate"] = "true"
            data["isSuper"] = 1
            data["recruitType"] = ""
            data["learnId"] = ""
            data["stdName"] = ""
            data["oldStdStage"] = 2
            data["pfsnLevel"] = 5
            data["assignFlag"] = 0
            data["groupManager"] = ""
            data["reason"] = ""
            return data
        else:
            print("入参错误！！")


    def get_addStudentOut_data(self):
        '''退学申请接口参数组装'''
        data = {"exType": (None, ""),"stdStage": (None, 2),
                "mobile": (None, ""),"uploadfile-1": (None, 2),"attachment": (None, ""),"remark": (None, "test_student_out!")}
        data["_web_token"]=(None, self.sread_xl('Web_token', 'L'))
        data["grade"]=(None, 2020)
        data["stdId"]=(None, self.sread_xl('CJdata', 'E'))
        data["learnId"]=(None, self.sread_xl('CJdata', 'D'))

        return data


    def get_passFinancialApproval(self):
        '''退学初审接口参数组装'''
        data={"exType":"UPDATE","grade":2020,"checkStatus":2,"financial_remark":""}
        data["learnId"] = self.sread_xl('CJdata', 'D')
        data["outId"]= self.sread_xl('CJdata', 'M')
        data["_web_token"] = self.sread_xl('Web_token', 'M')
        data["reason"] = "成考未通过"
        data["items[0].itemCode"] = "Y0"
        data["items[0].refundAmount"] = 100.00
        return data

    def get_passSchoolManagedApproval(self):
        '''退学终审接口参数组装'''
        data={"exType":"UPDATE","grade":2020,"checkStatus":2,"schoolManagedRemark":""}
        data["learnId"] = self.sread_xl('CJdata', 'D')
        data["outId"]= self.sread_xl('CJdata', 'M')
        data["_web_token"] = self.sread_xl('Web_token', 'M')
        data["reason"] = "成考未通过"
        data["items[0].itemCode"] = "Y0"
        data["items[0].refundAmount"] = 100.00
        return data



if __name__ == '__main__':
    print(GetTestData().get_updateStudentScore_data())
    # print(GetTestData().get_updateAnnex_data(1))
    # print(GetTestData().get_updateAnnex_data(2))
    # print(GetTestData().get_updateAnnex_data(3))