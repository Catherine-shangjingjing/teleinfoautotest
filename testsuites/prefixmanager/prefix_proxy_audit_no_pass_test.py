# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/prefixmanager/prefix_proxy_audit_no_pass.yml


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

from testcases.prefixmanager.ent_prefix_manage_pageQuery_no_proxy_test import (
    TestCaseEntPrefixManagePagequeryNoProxy as EntPrefixManagePagequeryNoProxy,
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

from testcases.prefixmanager.proxy_server_pageQuery_test import (
    TestCaseProxyServerPagequery as ProxyServerPagequery,
)

from testcases.prefixmanager.ent_prefix_proxy_audit_no_pass_test import (
    TestCaseEntPrefixProxyAuditNoPass as EntPrefixProxyAuditNoPass,
)

from testcases.prefixmanager.ent_prefix_manage_pageQuery_rejected_test import (
    TestCaseEntPrefixManagePagequeryRejected as EntPrefixManagePagequeryRejected,
)


class TestCasePrefixProxyAuditNoPass(HttpRunner):

    config = Config("前缀托管审核不通过").variables(
        **{
            "email": "${get_email()}",
            "mobile": "${get_mobile()}",
            "username": "${get_username()}",
            "account": "${ENV(adminaccount)}",
            "password": "${ENV(adminpassword)}",
            "entaccount": "$username",
            "entpassword": "${ENV(entpassword)}",
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
                    "entInfoSyss_2_deployAddrCity",
                    "entApplyId",
                    "contactCrtNo",
                    "contactName",
                    "orgNatureDesc",
                    "orgAddrCity",
                    "legalPhone",
                    "orgAddrProvinceDesc",
                    "imgId_f",
                    "entInfoSyss_1_id",
                    "entInfoSyss_3_deployAddr",
                    "entInfoSyss_0_sysType",
                    "orgAddrProvince",
                    "updateDate",
                    "orgCrtType",
                    "legalEmail",
                    "userId",
                    "entUserId",
                    "entInfoSyss_1_entApplyId",
                    "orgName",
                    "orgNature",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_2_id",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_1_deployAddr",
                    "orgCrtImgRid",
                    "entInfoSyss_0_deployAddr",
                    "applyId",
                    "industryCategory",
                    "entId",
                    "legalCrtType",
                    "orgAddrCityDesc",
                    "contactEmail",
                    "prefix",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_1_sysType",
                    "createDate",
                    "entInfoSyss_3_sysType",
                    "orgAddrCounty",
                    "orgCrtCode",
                    "imgId",
                    "orgAddr",
                    "entInfoSyss_1_deployAddrCounty",
                    "legalCrtTypeDesc",
                    "entInfoSyss_0_deployAddrCounty",
                    "orgAddrCountyDesc",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_2_deployMode",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_0_deployMode",
                    "legalName",
                    "entInfoSyss_3_entApplyId",
                    "contactCrtType",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCity",
                    "contactPhone",
                    "legalCrtNo",
                    "imgId_b",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_0_id",
                    "industrySpecific",
                    "entInfoSyss_3_id",
                    "entInfoSyss_2_deployAddrCounty",
                    "userName",
                    "entInfoSyss_2_deployAddr",
                    "legalCrtBackImgRid",
                    "entInfoSyss_1_deployAddrCity",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "entInfoSyss_2_deployAddrCity",
                    "entApplyId",
                    "contactCrtNo",
                    "contactName",
                    "orgNatureDesc",
                    "orgAddrCity",
                    "legalPhone",
                    "orgAddrProvinceDesc",
                    "imgId_f",
                    "entInfoSyss_1_id",
                    "entInfoSyss_3_deployAddr",
                    "entInfoSyss_0_sysType",
                    "orgAddrProvince",
                    "updateDate",
                    "orgCrtType",
                    "legalEmail",
                    "userId",
                    "entUserId",
                    "entInfoSyss_1_entApplyId",
                    "orgName",
                    "orgNature",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_2_id",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_1_deployAddr",
                    "orgCrtImgRid",
                    "entInfoSyss_0_deployAddr",
                    "applyId",
                    "industryCategory",
                    "entId",
                    "legalCrtType",
                    "orgAddrCityDesc",
                    "contactEmail",
                    "prefix",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_1_sysType",
                    "createDate",
                    "entInfoSyss_3_sysType",
                    "orgAddrCounty",
                    "orgCrtCode",
                    "imgId",
                    "orgAddr",
                    "entInfoSyss_1_deployAddrCounty",
                    "legalCrtTypeDesc",
                    "entInfoSyss_0_deployAddrCounty",
                    "orgAddrCountyDesc",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_2_deployMode",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_0_deployMode",
                    "legalName",
                    "entInfoSyss_3_entApplyId",
                    "contactCrtType",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCity",
                    "contactPhone",
                    "legalCrtNo",
                    "imgId_b",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_0_id",
                    "industrySpecific",
                    "entInfoSyss_3_id",
                    "entInfoSyss_2_deployAddrCounty",
                    "userName",
                    "entInfoSyss_2_deployAddr",
                    "legalCrtBackImgRid",
                    "entInfoSyss_1_deployAddrCity",
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
        Step(RunTestCase("前缀管理分页-未托管或者驳回").call(EntPrefixManagePagequeryNoProxy)),
        Step(RunTestCase("企业登陆").call(LoginEnt).export(*["entSession"])),
        Step(RunTestCase("申请托管").call(EntProxyApply)),
        Step(RunTestCase("管理员登陆").call(LoginAdmin).export(*["adminSession"])),
        Step(RunTestCase("前缀管理分页-待审核").call(EntPrefixManagePagequeryAudit)),
        Step(
            RunTestCase("托管审核分页").call(EntPrefixProxyAudit).export(*["prefixauditid"])
        ),
        Step(
            RunTestCase("托管服务器获取").call(ProxyServerPagequery).export(*["proxyServerId"])
        ),
        Step(RunTestCase("托管审核不通过").call(EntPrefixProxyAuditNoPass)),
        Step(RunTestCase("前缀管理分页-驳回").call(EntPrefixManagePagequeryRejected)),
    ]


if __name__ == "__main__":
    TestCasePrefixProxyAuditNoPass().test_start()
