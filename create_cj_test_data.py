from test_case.test_01_recruitAdd import *
import sys

def addtestdata(num):
    RecruitAddTest().test_00_login()

    for i in range(0,num):
        RecruitAddTest().test_01_cj_recruit_webtoken()
        RecruitAddTest().test_02_cj_recruit()
        # RecruitAddTest().test_03_gk_recruit_webtoken()
        # RecruitAddTest().test_04_gk_recruit()
if __name__ == '__main__':
    # num = sys.argv[1]
    addtestdata(1)