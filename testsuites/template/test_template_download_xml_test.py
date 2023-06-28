# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/template/test_template_download_xml.yml


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

from testcases.handle.handleXmlTemplateDownload_test import (
    TestCaseHandlexmltemplatedownload as Handlexmltemplatedownload,
)


class TestCaseTestTemplateDownloadXml(HttpRunner):

    config = Config("xml下载").variables(
        **{
            "handle": "${prefix}/${get_random_param(100000,1000000,1)}",
            "version": "zjauto${get_random_param(1,10000,1)}",
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
                    "entInfoSyss_2_deployAddrCity",
                    "contactName",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_1_deployAddrCity",
                    "orgAddrCityDesc",
                    "entApplyId",
                    "entInfoSyss_3_deployAddrProvince",
                    "legalCrtTypeDesc",
                    "entInfoSyss_2_deployMode",
                    "orgName",
                    "entUserId",
                    "prefix",
                    "imgId_f",
                    "entInfoSyss_1_deployAddr",
                    "orgAddr",
                    "userId",
                    "legalEmail",
                    "orgAddrCounty",
                    "orgCrtType",
                    "orgCrtCode",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_3_deployAddr",
                    "contactCrtType",
                    "applyId",
                    "contactEmail",
                    "updateDate",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_0_deployMode",
                    "industrySpecific",
                    "entInfoSyss_2_deployAddrCounty",
                    "userName",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_1_deployMode",
                    "industryCategory",
                    "contactPhone",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_deployAddrCounty",
                    "imgId",
                    "entInfoSyss_1_id",
                    "orgNatureDesc",
                    "entInfoSyss_0_id",
                    "entInfoSyss_0_deployAddr",
                    "imgId_b",
                    "orgAddrCity",
                    "orgCrtImgRid",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_1_deployAddrProvince",
                    "legalPhone",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_2_entApplyId",
                    "orgCategorySpecificDesc",
                    "orgAddrProvinceDesc",
                    "legalCrtType",
                    "entInfoSyss_3_id",
                    "entId",
                    "legalCrtBackImgRid",
                    "createDate",
                    "legalCrtNo",
                    "entInfoSyss_2_sysType",
                    "orgNature",
                    "orgAddrProvince",
                    "contactCrtNo",
                    "entInfoSyss_0_deployAddrCity",
                    "orgAddrCountyDesc",
                    "entInfoSyss_2_deployAddr",
                    "legalName",
                    "entInfoSyss_3_deployAddrCity",
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
                    "contactName",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_1_deployAddrCity",
                    "orgAddrCityDesc",
                    "entApplyId",
                    "entInfoSyss_3_deployAddrProvince",
                    "legalCrtTypeDesc",
                    "entInfoSyss_2_deployMode",
                    "orgName",
                    "entUserId",
                    "prefix",
                    "imgId_f",
                    "entInfoSyss_1_deployAddr",
                    "orgAddr",
                    "userId",
                    "legalEmail",
                    "orgAddrCounty",
                    "orgCrtType",
                    "orgCrtCode",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_3_deployAddr",
                    "contactCrtType",
                    "applyId",
                    "contactEmail",
                    "updateDate",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_0_deployMode",
                    "industrySpecific",
                    "entInfoSyss_2_deployAddrCounty",
                    "userName",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_1_deployMode",
                    "industryCategory",
                    "contactPhone",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_deployAddrCounty",
                    "imgId",
                    "entInfoSyss_1_id",
                    "orgNatureDesc",
                    "entInfoSyss_0_id",
                    "entInfoSyss_0_deployAddr",
                    "imgId_b",
                    "orgAddrCity",
                    "orgCrtImgRid",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_1_deployAddrProvince",
                    "legalPhone",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_2_entApplyId",
                    "orgCategorySpecificDesc",
                    "orgAddrProvinceDesc",
                    "legalCrtType",
                    "entInfoSyss_3_id",
                    "entId",
                    "legalCrtBackImgRid",
                    "createDate",
                    "legalCrtNo",
                    "entInfoSyss_2_sysType",
                    "orgNature",
                    "orgAddrProvince",
                    "contactCrtNo",
                    "entInfoSyss_0_deployAddrCity",
                    "orgAddrCountyDesc",
                    "entInfoSyss_2_deployAddr",
                    "legalName",
                    "entInfoSyss_3_deployAddrCity",
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
            .export(*["entPrefix", "entNameCn", "proxyState", "userId", "prefixId"])
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
            .export(*["template_handle", "template_id"])
        ),
        Step(RunTestCase("xml模版下载").call(Handlexmltemplatedownload)),
    ]


if __name__ == "__main__":
    TestCaseTestTemplateDownloadXml().test_start()