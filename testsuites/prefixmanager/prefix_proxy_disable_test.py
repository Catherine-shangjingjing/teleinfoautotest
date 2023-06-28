# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/prefixmanager/prefix_proxy_disable.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.prefixAudit.register_test import TestCaseRegister as Register

from testcases.login.login_ent_test import TestCaseLoginEnt as LoginEnt

from testcases.prefixAudit.register.upload_img_test import (
    TestCaseUploadImg as UploadImg,
)

from testcases.prefixAudit.register.upload_img_f_test import (
    TestCaseUploadImgF as UploadImgF,
)

from testcases.prefixAudit.register.upload_img_b_test import (
    TestCaseUploadImgB as UploadImgB,
)

from testcases.prefixAudit.register.submit_first_test import (
    TestCaseSubmitFirst as SubmitFirst,
)

from testcases.prefixAudit.register.apply_or_not_test import (
    TestCaseApplyOrNot as ApplyOrNot,
)

from testcases.prefixAudit.register.submit_second_test import (
    TestCaseSubmitSecond as SubmitSecond,
)

from testcases.prefixAudit.register.submit_final_test import (
    TestCaseSubmitFinal as SubmitFinal,
)

from testcases.login.login_admin_test import TestCaseLoginAdmin as LoginAdmin

from testcases.prefixAudit.audit.finance_rule_findRule_test import (
    TestCaseFinanceRuleFindrule as FinanceRuleFindrule,
)

from testcases.prefixAudit.audit.finance_rule_findRule_reg_test import (
    TestCaseFinanceRuleFindruleReg as FinanceRuleFindruleReg,
)

from testcases.prefixAudit.audit.v3_ent_audit_save_test import (
    TestCaseV3EntAuditSave as V3EntAuditSave,
)

from testcases.prefixAlloc.ent_prefix_alloc_pageQuery_1_test import (
    TestCaseEntPrefixAllocPagequery1 as EntPrefixAllocPagequery1,
)

from testcases.prefixAlloc.ent_prefix_alloc_savePrefix_test import (
    TestCaseEntPrefixAllocSaveprefix as EntPrefixAllocSaveprefix,
)

from testcases.prefixmanager.ent_proxy_apply_test import (
    TestCaseEntProxyApply as EntProxyApply,
)

from testcases.prefixmanager.ent_prefix_manage_pageQuery_audit_test import (
    TestCaseEntPrefixManagePagequeryAudit as EntPrefixManagePagequeryAudit,
)

from testcases.prefixmanager.ent_prefix_proxy_audit_test import (
    TestCaseEntPrefixProxyAudit as EntPrefixProxyAudit,
)

from testcases.proxyAudit.proxyserverlist_test import (
    TestCaseProxyserverlist as Proxyserverlist,
)

from testcases.proxyAudit.proxyserverprefixaudit_test import (
    TestCaseProxyserverprefixaudit as Proxyserverprefixaudit,
)

from testcases.prefixmanager.ent_prefix_manage_pageQuery_entPrefix_test import (
    TestCaseEntPrefixManagePagequeryEntprefix as EntPrefixManagePagequeryEntprefix,
)

from testcases.prefixmanager.ent_prefix_manage_stateChange_disable_test import (
    TestCaseEntPrefixManageStatechangeDisable as EntPrefixManageStatechangeDisable,
)

from testcases.prefixmanager.ent_prefix_manage_pageQuery_disable_test import (
    TestCaseEntPrefixManagePagequeryDisable as EntPrefixManagePagequeryDisable,
)

from testcases.idhub.idhub_regist_handle_no_pass_test import (
    TestCaseIdhubRegistHandleNoPass as IdhubRegistHandleNoPass,
)

from testcases.idhub.idhub_parse_no_pass_test import (
    TestCaseIdhubParseNoPass as IdhubParseNoPass,
)

from testcases.logmanager.log_operation_pageQuery_disable_test import (
    TestCaseLogOperationPagequeryDisable as LogOperationPagequeryDisable,
)

from testcases.prefixmanager.ent_prefix_manage_stateChange_enable_test import (
    TestCaseEntPrefixManageStatechangeEnable as EntPrefixManageStatechangeEnable,
)

from testcases.idhub.idhub_regist_handle_pass_test import (
    TestCaseIdhubRegistHandlePass as IdhubRegistHandlePass,
)

from testcases.idhub.idhub_parse_pass_test import (
    TestCaseIdhubParsePass as IdhubParsePass,
)


class TestCasePrefixProxyDisable(HttpRunner):

    config = Config("前缀管理列表").variables(
        **{
            "email": "${get_email()}",
            "mobile": "${get_mobile()}",
            "username": "${get_username()}",
            "account": "${ENV(adminaccount)}",
            "password": "${ENV(adminpassword)}",
            "entaccount": "$username",
            "entpassword": "${ENV(entpassword)}",
            "moneyType1": 1,
            "moneyType2": 2,
            "biaoshi": "${get_random_param(10000,1000000,1)}",
            "idhub_biaoshi": "$pendingPrefixCondition/$biaoshi",
            "operation": "",
            "operationObj": "",
            "pendingPrefixCondition": "${ENV(prefix_second)}${get_random_param(1000,10000000000,1)}",
            "prefix": "${ENV(prefix_second)}${get_random_param(1000,10000000000,1)}",
            "personId": "${get_idcardno()}",
        }
    )

    teststeps = [
        Step(RunTestCase("用户注册").call(Register)),
        Step(RunTestCase("登录-企业").call(LoginEnt).export(*["entSession"])),
        Step(RunTestCase("前缀注册企业资质图片上传").call(UploadImg).export(*["imgId"])),
        Step(RunTestCase("前缀注册企业联系人身份证图片正面上传").call(UploadImgF).export(*["imgId_f"])),
        Step(RunTestCase("前缀注册企业联系人身份证图片背面上传").call(UploadImgB).export(*["imgId_b"])),
        Step(RunTestCase("企业注册第一步提交信息").call(SubmitFirst)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "contactCrtNo",
                    "imgId",
                    "createDate",
                    "entInfoSyss_0_deployAddrCity",
                    "orgAddr",
                    "legalName",
                    "entApplyId",
                    "orgCrtType",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_2_deployAddrCounty",
                    "imgId_f",
                    "entInfoSyss_3_id",
                    "legalEmail",
                    "contactPhone",
                    "orgAddrCountyDesc",
                    "legalCrtTypeDesc",
                    "updateDate",
                    "industrySpecific",
                    "legalCrtType",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_3_sysType",
                    "legalPhone",
                    "entInfoSyss_3_deployAddr",
                    "contactCrtType",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_0_deployAddrCounty",
                    "entUserId",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_2_entApplyId",
                    "entId",
                    "imgId_b",
                    "userName",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_2_deployAddrCity",
                    "entInfoSyss_3_deployAddrCounty",
                    "industryCategory",
                    "orgCrtCode",
                    "entInfoSyss_1_deployAddrCounty",
                    "orgAddrCounty",
                    "orgAddrCity",
                    "entInfoSyss_1_deployAddr",
                    "legalCrtNo",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_1_sysType",
                    "orgNatureDesc",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_2_deployAddr",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_2_sysType",
                    "orgAddrProvinceDesc",
                    "orgAddrCityDesc",
                    "userId",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_deployAddrCity",
                    "contactEmail",
                    "prefix",
                    "orgName",
                    "entInfoSyss_3_deployAddrProvince",
                    "orgCrtImgRid",
                    "entInfoSyss_0_id",
                    "contactName",
                    "entInfoSyss_1_id",
                    "orgNature",
                    "applyId",
                    "legalCrtBackImgRid",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "contactCrtNo",
                    "imgId",
                    "createDate",
                    "entInfoSyss_0_deployAddrCity",
                    "orgAddr",
                    "legalName",
                    "entApplyId",
                    "orgCrtType",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_2_deployAddrCounty",
                    "imgId_f",
                    "entInfoSyss_3_id",
                    "legalEmail",
                    "contactPhone",
                    "orgAddrCountyDesc",
                    "legalCrtTypeDesc",
                    "updateDate",
                    "industrySpecific",
                    "legalCrtType",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_3_sysType",
                    "legalPhone",
                    "entInfoSyss_3_deployAddr",
                    "contactCrtType",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_0_deployAddrCounty",
                    "entUserId",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_2_entApplyId",
                    "entId",
                    "imgId_b",
                    "userName",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_2_deployAddrCity",
                    "entInfoSyss_3_deployAddrCounty",
                    "industryCategory",
                    "orgCrtCode",
                    "entInfoSyss_1_deployAddrCounty",
                    "orgAddrCounty",
                    "orgAddrCity",
                    "entInfoSyss_1_deployAddr",
                    "legalCrtNo",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_1_sysType",
                    "orgNatureDesc",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_2_deployAddr",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_2_sysType",
                    "orgAddrProvinceDesc",
                    "orgAddrCityDesc",
                    "userId",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_deployAddrCity",
                    "contactEmail",
                    "prefix",
                    "orgName",
                    "entInfoSyss_3_deployAddrProvince",
                    "orgCrtImgRid",
                    "entInfoSyss_0_id",
                    "contactName",
                    "entInfoSyss_1_id",
                    "orgNature",
                    "applyId",
                    "legalCrtBackImgRid",
                ]
            )
        ),
        Step(RunTestCase("企业注册最终第三步提交信息").call(SubmitFinal)),
        Step(RunTestCase("登录-管理员").call(LoginAdmin).export(*["adminSession"])),
        Step(
            RunTestCase("年费费用查询").call(FinanceRuleFindrule).export(*["annualFeeRuleId"])
        ),
        Step(
            RunTestCase("注册费费用查询")
            .call(FinanceRuleFindruleReg)
            .export(*["regFeeRuleId"])
        ),
        Step(RunTestCase("前缀审核结果保存").call(V3EntAuditSave)),
        Step(
            RunTestCase("前缀分配列表")
            .call(EntPrefixAllocPagequery1)
            .export(*["userId", "orgName"])
        ),
        Step(
            RunTestCase("收费标准查询-注册费")
            .call(FinanceRuleFindruleReg)
            .export(*["regFeeRuleId"])
        ),
        Step(
            RunTestCase("收费标准查询-年费")
            .call(FinanceRuleFindrule)
            .export(*["annualFeeRuleId"])
        ),
        Step(RunTestCase("保存分配前缀").call(EntPrefixAllocSaveprefix)),
        Step(RunTestCase("企业登陆").call(LoginEnt).export(*["entSession"])),
        Step(RunTestCase("申请托管").call(EntProxyApply)),
        Step(RunTestCase("管理员登陆").call(LoginAdmin).export(*["adminSession"])),
        Step(RunTestCase("前缀管理分页-待审核").call(EntPrefixManagePagequeryAudit)),
        Step(
            RunTestCase("托管审核分页").call(EntPrefixProxyAudit).export(*["prefixauditid"])
        ),
        Step(RunTestCase("托管服务器获取").call(Proxyserverlist).export(*["proxyserverid"])),
        Step(RunTestCase("托管审核通过").call(Proxyserverprefixaudit)),
        Step(
            RunTestCase("前缀管理分页-前缀查询")
            .call(EntPrefixManagePagequeryEntprefix)
            .export(*["prefixId", "orgName"])
        ),
        Step(RunTestCase("停用前缀").call(EntPrefixManageStatechangeDisable)),
        Step(RunTestCase("前缀管理分页-停用").call(EntPrefixManagePagequeryDisable)),
        Step(RunTestCase("调用idhub接口创建标识1条").call(IdhubRegistHandleNoPass)),
        Step(RunTestCase("调用idhub接口解析标识1条").call(IdhubParseNoPass)),
        Step(RunTestCase("操作日志列表").call(LogOperationPagequeryDisable)),
        Step(RunTestCase("启用前缀").call(EntPrefixManageStatechangeEnable)),
        Step(RunTestCase("调用idhub接口创建标识1条").call(IdhubRegistHandlePass)),
        Step(RunTestCase("调用idhub接口解析标识1条").call(IdhubParsePass)),
    ]


if __name__ == "__main__":
    TestCasePrefixProxyDisable().test_start()
