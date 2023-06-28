#!/bin/bash
echo "******************开始批量执行测试用例******************"

hrun testsuites/statistic/biaoshiStatistic.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/biaoshiStatistic_registertop10.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/datamanager_biaoshiStatistic_parse.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/ent_biaoshiStatistic.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/handle_prase_num.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/handle_reglist_top_10.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/handle_stocknum_registernum.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/proxy_biaoshiStatistic.yml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/selfIdhub-admin.yaml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/selfIdhub-ent.yaml --alluredir=reports/allure_results_stat
hrun testsuites/statistic/test_handle_statistic_ent.yml --alluredir=reports/allure_results_stat

echo "******************批量执行测试用例完毕******************"
echo "******************开始生成报告******************"
allure generate --clean reports/allure_results_stat -o reports/allure_reports_stat
echo "******************生成报告完成******************"