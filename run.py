import pytest
import os
import time

if __name__ == '__main__':
    # pytest.main(["testsuites",
    #              "--alluredir", "reports/allure_results"])
    os.system("hrun testsuites/applyRecord/  --alluredir=reports/allure_results --clean-alluredir")
    time.sleep(1)
    os.system(r"allure generate --clean reports/allure_results -o reports/allure_reports")