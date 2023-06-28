#!/bin/bash
echo "******************开始批量执行测试用例******************"

hrun testsuites/applyRecord/entApply-ent.yml --alluredir=reports/allure_results
hrun testsuites/applyRecord/entApply-admin.yml --alluredir=reports/allure_results
hrun testsuites/checkFlow/check_prefix_fail.yml --alluredir=reports/allure_results #接口有次数限制，非必要少跑
hrun testsuites/checkFlow/check_prefix_success.yml --alluredir=reports/allure_results #接口有次数限制，非必要少跑
hrun testsuites/checkhandle/checkHandleDel.yml --alluredir=reports/allure_results
hrun testsuites/checkhandle/checkId_adopt.yml --alluredir=reports/allure_results
hrun testsuites/checkhandle/checkId_exist.yml --alluredir=reports/allure_results
hrun testsuites/checkhandle/checkId_format.yml --alluredir=reports/allure_results
hrun testsuites/entapply/apply_again.yml --alluredir=reports/allure_results
hrun testsuites/entapply/register.yml --alluredir=reports/allure_results
hrun testsuites/entapply/register_wrong.yml --alluredir=reports/allure_results
hrun testsuites/entapply/store.yml --alluredir=reports/allure_results
hrun testsuites/entapply/store_final.yml --alluredir=reports/allure_results
hrun testsuites/entapply/store_second.yml --alluredir=reports/allure_results
hrun testsuites/entapply/store_wrong.yml --alluredir=reports/allure_results
hrun testsuites/entapply/update.yml --alluredir=reports/allure_results
hrun testsuites/entBusiness/entBusinessOpe.yaml --alluredir=reports/allure_results
hrun testsuites/entBusiness/entBusinessPage-admin.yaml --alluredir=reports/allure_results
hrun testsuites/handle/test_handle_detail.yml --alluredir=reports/allure_results
hrun testsuites/handle/test_handle_resolve_withChineseValue.yml --alluredir=reports/allure_results
hrun testsuites/handle/test_handle_update_delete.yml --alluredir=reports/allure_results
hrun testsuites/homepage/ent_applying.yml --alluredir=reports/allure_results
hrun testsuites/homepage/ent_register.yml --alluredir=reports/allure_results
#hrun testsuites/homepage/handle_reglist_top_10.yml --alluredir=reports/allure_results
#hrun testsuites/idhub/selfIdhub-admin.yaml --alluredir=reports/allure_results
#hrun testsuites/idhub/selfIdhub-ent.yaml --alluredir=reports/allure_results
hrun testsuites/logmanager/apply_epplog.yml --alluredir=reports/allure_results
hrun testsuites/logmanager/userlog.yml --alluredir=reports/allure_results
hrun testsuites/prefixAlloc/prefixAlloc-10.yaml --alluredir=reports/allure_results
hrun testsuites/prefixAlloc/prefixAllocLog.yaml --alluredir=reports/allure_results
hrun testsuites/prefixAlloc/prefixAllocPage.yaml --alluredir=reports/allure_results
hrun testsuites/prefixAudit/prefix_audit_pageQuery_auditState_no_pass.yml --alluredir=reports/allure_results
hrun testsuites/prefixAudit/prefix_audit_pageQuery_auditState_pass.yml --alluredir=reports/allure_results
hrun testsuites/prefixAudit/prefix_audit_pageQuery_orgName.yml --alluredir=reports/allure_results
hrun testsuites/prefixAudit/prefix_register.yml --alluredir=reports/allure_results
#hrun testsuites/prefixAudit/prefix_rejected.yml --alluredir=reports/allure_results 用例重复
hrun testsuites/prefixAudit/prefixAudit.yaml --alluredir=reports/allure_results
hrun testsuites/prefixAudit/prefixRejected.yaml --alluredir=reports/allure_results
hrun testsuites/prefixAudit/test_update_prefix_audit_success.yml --alluredir=reports/allure_results
hrun testsuites/prefixmanager/prefix_config_add_v4.yml --alluredir=reports/allure_results
hrun testsuites/prefixmanager/prefix_config_modify_v6.yml --alluredir=reports/allure_results
hrun testsuites/prefixmanager/prefix_manager_query.yml --alluredir=reports/allure_results
hrun testsuites/prefixmanager/prefix_proxy_audit_no_pass.yml --alluredir=reports/allure_results
hrun testsuites/prefixmanager/prefix_proxy_audit_pass.yml --alluredir=reports/allure_results
hrun testsuites/prefixmanager/prefix_proxy_delete.yml --alluredir=reports/allure_results
hrun testsuites/prefixmanager/prefix_proxy_disable.yml --alluredir=reports/allure_results
hrun testsuites/proxyAudit/proxyserveraudit.yml --alluredir=reports/allure_results
hrun testsuites/proxyAudit/proxyserverauditcancel.yml --alluredir=reports/allure_results
hrun testsuites/proxyAudit/proxyserverauditcancel_ent.yml --alluredir=reports/allure_results
hrun testsuites/proxyAudit/test_proxyserver_audit_cancle_ent.yml --alluredir=reports/allure_results
hrun testsuites/proxyAudit/test_proxyserver_audit_reject_detail.yml --alluredir=reports/allure_results
hrun testsuites/proxyAudit/test_proxyserver_audit_sumbit.yml --alluredir=reports/allure_results
hrun testsuites/template/test_template_delete.yml --alluredir=reports/allure_results
hrun testsuites/template/test_template_delete_noupload.yml --alluredir=reports/allure_results
hrun testsuites/template/test_template_detail.yml --alluredir=reports/allure_results
hrun testsuites/template/test_template_download_excel.yml --alluredir=reports/allure_results
hrun testsuites/template/test_template_download_xml.yml --alluredir=reports/allure_results
hrun testsuites/template/test_template_update.yml --alluredir=reports/allure_results
hrun testsuites/template/test_template_upload.yml --alluredir=reports/allure_results
hrun testsuites/uploadfile/test_upload_excel.yml --alluredir=reports/allure_results
hrun testsuites/uploadfile/test_upload_xml.yml --alluredir=reports/allure_results


echo "******************批量执行测试用例完毕******************"
echo "******************开始生成报告******************"
allure generate --clean reports/allure_results -o reports/allure_reports
echo "******************生成报告完成******************"
