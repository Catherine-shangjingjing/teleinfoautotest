# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/template/test_template_update.yml


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

from testcases.prefixAudit.audit.ent_prefix_manage_pageQuery_prefix_test import (
    TestCaseEntPrefixManagePagequeryPrefix as EntPrefixManagePagequeryPrefix,
)

from testcases.proxyAudit.proxy_apply_test import TestCaseProxyApply as ProxyApply

from testcases.prefixAudit.proxyserverauditlist_test import (
    TestCaseProxyserverauditlist as Proxyserverauditlist,
)

from testcases.proxyAudit.proxyserverlist_test import (
    TestCaseProxyserverlist as Proxyserverlist,
)

from testcases.proxyAudit.proxyserverprefixaudit_test import (
    TestCaseProxyserverprefixaudit as Proxyserverprefixaudit,
)

from testcases.template.templateCreate_test import (
    TestCaseTemplatecreate as Templatecreate,
)

from testcases.template.templateQuery_test import TestCaseTemplatequery as Templatequery

from testcases.template.templateUpdate_test import (
    TestCaseTemplateupdate as Templateupdate,
)


class TestCaseTestTemplateUpdate(HttpRunner):

    config = Config("托管标识详情-5").variables(
        **{
            "handle": "${prefix}/${get_random_param(100000,1000000,1)}",
            "version": "zjauto${get_random_param(100000000,100000000000,1)}",
            "email": "${get_email()}",
            "mobile": "${get_mobile()}",
            "username": "${get_username()}",
            "account": "${ENV(adminaccount)}",
            "password": "${ENV(adminpassword)}",
            "entaccount": "$username",
            "entpassword": "${ENV(entpassword)}",
            "prefix": "${ENV(prefix_second)}${get_random_param(1,10000000000,1)}",
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
                    "entInfoSyss_2_sysType",
                    "orgCategorySpecificDesc",
                    "imgId",
                    "entInfoSyss_0_deployMode",
                    "contactPhone",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_2_deployAddrCounty",
                    "updateDate",
                    "entInfoSyss_3_entApplyId",
                    "prefix",
                    "orgCrtCode",
                    "entInfoSyss_3_deployAddrCity",
                    "entInfoSyss_1_deployAddr",
                    "industryCategory",
                    "entInfoSyss_2_deployAddrProvince",
                    "legalEmail",
                    "orgAddrCounty",
                    "legalCrtFrontImgRid",
                    "contactName",
                    "entInfoSyss_0_deployAddrProvince",
                    "legalName",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_2_deployAddrCity",
                    "industrySpecific",
                    "orgAddrCity",
                    "userId",
                    "orgName",
                    "legalCrtType",
                    "orgNatureDesc",
                    "orgAddrProvinceDesc",
                    "orgCrtType",
                    "createDate",
                    "entInfoSyss_0_id",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_1_deployAddrCity",
                    "contactCrtNo",
                    "orgAddrCountyDesc",
                    "entInfoSyss_1_deployAddrCounty",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_1_id",
                    "userName",
                    "orgAddr",
                    "contactEmail",
                    "orgAddrCityDesc",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_3_id",
                    "entId",
                    "contactCrtType",
                    "entInfoSyss_1_deployMode",
                    "applyId",
                    "entInfoSyss_0_deployAddrCity",
                    "orgNature",
                    "legalPhone",
                    "legalCrtBackImgRid",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_3_deployMode",
                    "legalCrtTypeDesc",
                    "entInfoSyss_0_deployAddr",
                    "imgId_f",
                    "entApplyId",
                    "entInfoSyss_3_deployAddr",
                    "legalCrtNo",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddrProvince",
                    "imgId_b",
                    "entInfoSyss_2_id",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_3_sysType",
                    "entUserId",
                    "orgCrtImgRid",
                    "orgAddrProvince",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "entInfoSyss_2_sysType",
                    "orgCategorySpecificDesc",
                    "imgId",
                    "entInfoSyss_0_deployMode",
                    "contactPhone",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_2_deployAddrCounty",
                    "updateDate",
                    "entInfoSyss_3_entApplyId",
                    "prefix",
                    "orgCrtCode",
                    "entInfoSyss_3_deployAddrCity",
                    "entInfoSyss_1_deployAddr",
                    "industryCategory",
                    "entInfoSyss_2_deployAddrProvince",
                    "legalEmail",
                    "orgAddrCounty",
                    "legalCrtFrontImgRid",
                    "contactName",
                    "entInfoSyss_0_deployAddrProvince",
                    "legalName",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_2_deployAddrCity",
                    "industrySpecific",
                    "orgAddrCity",
                    "userId",
                    "orgName",
                    "legalCrtType",
                    "orgNatureDesc",
                    "orgAddrProvinceDesc",
                    "orgCrtType",
                    "createDate",
                    "entInfoSyss_0_id",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_1_deployAddrCity",
                    "contactCrtNo",
                    "orgAddrCountyDesc",
                    "entInfoSyss_1_deployAddrCounty",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_1_id",
                    "userName",
                    "orgAddr",
                    "contactEmail",
                    "orgAddrCityDesc",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_3_id",
                    "entId",
                    "contactCrtType",
                    "entInfoSyss_1_deployMode",
                    "applyId",
                    "entInfoSyss_0_deployAddrCity",
                    "orgNature",
                    "legalPhone",
                    "legalCrtBackImgRid",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_3_deployMode",
                    "legalCrtTypeDesc",
                    "entInfoSyss_0_deployAddr",
                    "imgId_f",
                    "entApplyId",
                    "entInfoSyss_3_deployAddr",
                    "legalCrtNo",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddrProvince",
                    "imgId_b",
                    "entInfoSyss_2_id",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_3_sysType",
                    "entUserId",
                    "orgCrtImgRid",
                    "orgAddrProvince",
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
        Step(RunTestCase("审核结果保存").call(V3EntAuditSave)),
        Step(
            RunTestCase("前缀管理分页")
            .call(EntPrefixManagePagequeryPrefix)
            .export(*["userId", "prefixId", "entNameCn", "proxyState", "entPrefix"])
        ),
        Step(RunTestCase("ent登录").call(LoginEnt).export(*["entSession"])),
        Step(RunTestCase("企业申请托管").call(ProxyApply)),
        Step(RunTestCase("admin登录").call(LoginAdmin).export(*["adminSession"])),
        Step(
            RunTestCase("前缀审核列表查询所申请前缀的id")
            .call(Proxyserverauditlist)
            .export(*["prefixauditid"])
        ),
        Step(RunTestCase("获取托管服务器列表").call(Proxyserverlist).export(*["proxyserverid"])),
        Step(RunTestCase("前缀审核通过").call(Proxyserverprefixaudit)),
        Step(RunTestCase("ent登录").call(LoginEnt).export(*["entSession"])),
        Step(RunTestCase("数据模板创建").call(Templatecreate)),
        Step(
            RunTestCase("数据模板查询")
            .call(Templatequery)
            .export(*["template_id", "template_handle"])
        ),
        Step(RunTestCase("数据模板更新").call(Templateupdate)),
    ]


if __name__ == "__main__":
    TestCaseTestTemplateUpdate().test_start()
