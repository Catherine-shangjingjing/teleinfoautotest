#!/bin/bash
#hmake testsuites/ysc/update/update.yml
pytest testsuites/ysc/update/update_test.py --alluredir=reports/allure_results --clean-alluredir
allure generate --clean reports/allure_results -o reports/allure_reports
echo "******************测试用例全量执行完毕******************"

