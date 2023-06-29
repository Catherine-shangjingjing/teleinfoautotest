import pytest
import os
import time

if __name__ == '__main__':
    print("******************开始批量执行测试用例******************")
    os.system("hrun testsuites/applyRecord/entApply-ent.yml --alluredir=reports/allure_results")
    os.system("hrun testsuites/applyRecord/entApply-admin.yml --alluredir=reports/allure_results")
    time.sleep(1)
    os.system(r"allure generate --clean reports/allure_results -o reports/allure_reports")