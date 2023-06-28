# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/statistic/test_handle_statistic_ent.yml


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

from testcases.statistics.ent_indexstatistics_test import (
    TestCaseEntIndexstatistics as EntIndexstatistics,
)

from testcases.template.templateCreate_test import (
    TestCaseTemplatecreate as Templatecreate,
)

from testcases.handle.handleCreate_ent_test import (
    TestCaseHandlecreateEnt as HandlecreateEnt,
)

from testcases.handle.resolveHandle_test import TestCaseResolvehandle as Resolvehandle

from testcases.statistics.ent_indexstatistics_2_test import (
    TestCaseEntIndexstatistics2 as EntIndexstatistics2,
)


class TestCaseTestHandleStatisticEnt(HttpRunner):

    config = Config("创建标识且解析该标识后查看企业首页标识统计-3、4").variables(
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
            "prefix": "${ENV(prefix_second)}${get_random_param(1,10000,1)}",
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
                    "entInfoSyss_2_deployAddrCounty",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_0_id",
                    "orgCrtImgRid",
                    "userName",
                    "entInfoSyss_2_deployAddrCity",
                    "legalEmail",
                    "applyId",
                    "contactEmail",
                    "userId",
                    "entUserId",
                    "entInfoSyss_1_deployAddr",
                    "contactPhone",
                    "orgName",
                    "legalCrtTypeDesc",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_0_deployAddr",
                    "legalName",
                    "orgAddrProvinceDesc",
                    "imgId_f",
                    "entInfoSyss_2_entApplyId",
                    "industryCategory",
                    "orgCrtType",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_3_id",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_3_entApplyId",
                    "orgAddrCityDesc",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCity",
                    "contactName",
                    "orgAddrCity",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_sysType",
                    "entId",
                    "orgNatureDesc",
                    "legalPhone",
                    "entInfoSyss_1_id",
                    "entInfoSyss_1_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "legalCrtBackImgRid",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCounty",
                    "orgNature",
                    "legalCrtNo",
                    "entInfoSyss_3_deployAddr",
                    "industrySpecific",
                    "imgId",
                    "entInfoSyss_1_deployMode",
                    "createDate",
                    "entInfoSyss_2_id",
                    "legalCrtFrontImgRid",
                    "orgAddrCountyDesc",
                    "prefix",
                    "orgCrtCode",
                    "contactCrtType",
                    "orgAddrCounty",
                    "updateDate",
                    "entApplyId",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_1_deployAddrCounty",
                    "orgAddr",
                    "entInfoSyss_0_deployAddrCity",
                    "legalCrtType",
                    "imgId_b",
                    "contactCrtNo",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "entInfoSyss_2_deployAddrCounty",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_0_id",
                    "orgCrtImgRid",
                    "userName",
                    "entInfoSyss_2_deployAddrCity",
                    "legalEmail",
                    "applyId",
                    "contactEmail",
                    "userId",
                    "entUserId",
                    "entInfoSyss_1_deployAddr",
                    "contactPhone",
                    "orgName",
                    "legalCrtTypeDesc",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_0_deployAddr",
                    "legalName",
                    "orgAddrProvinceDesc",
                    "imgId_f",
                    "entInfoSyss_2_entApplyId",
                    "industryCategory",
                    "orgCrtType",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_3_id",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_3_entApplyId",
                    "orgAddrCityDesc",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCity",
                    "contactName",
                    "orgAddrCity",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_sysType",
                    "entId",
                    "orgNatureDesc",
                    "legalPhone",
                    "entInfoSyss_1_id",
                    "entInfoSyss_1_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "legalCrtBackImgRid",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_2_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCounty",
                    "orgNature",
                    "legalCrtNo",
                    "entInfoSyss_3_deployAddr",
                    "industrySpecific",
                    "imgId",
                    "entInfoSyss_1_deployMode",
                    "createDate",
                    "entInfoSyss_2_id",
                    "legalCrtFrontImgRid",
                    "orgAddrCountyDesc",
                    "prefix",
                    "orgCrtCode",
                    "contactCrtType",
                    "orgAddrCounty",
                    "updateDate",
                    "entApplyId",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_1_deployAddrCounty",
                    "orgAddr",
                    "entInfoSyss_0_deployAddrCity",
                    "legalCrtType",
                    "imgId_b",
                    "contactCrtNo",
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
            .export(*["entPrefix", "prefixId", "proxyState", "entNameCn", "userId"])
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
        Step(
            RunTestCase("企业用户首页统计数据")
            .call(EntIndexstatistics)
            .export(
                *[
                    "identityNum",
                    "todayIdentityNum",
                    "delnum",
                    "resolvnum",
                    "todayResolvNum",
                ]
            )
        ),
        Step(RunTestCase("数据模板创建").call(Templatecreate)),
        Step(
            RunTestCase("企业用户首页统计数据")
            .call(EntIndexstatistics)
            .export(
                *[
                    "identityNum",
                    "todayIdentityNum",
                    "delnum",
                    "resolvnum",
                    "todayResolvNum",
                ]
            )
        ),
        Step(RunTestCase("标识注册").call(HandlecreateEnt)),
        Step(RunTestCase("门户首页递归解析已创建的标识").call(Resolvehandle)),
        Step(RunTestCase("企业用户首页统计数据").call(EntIndexstatistics2)),
    ]


if __name__ == "__main__":
    TestCaseTestHandleStatisticEnt().test_start()