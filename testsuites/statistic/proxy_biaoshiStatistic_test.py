# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/statistic/proxy_biaoshiStatistic.yml


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

from testcases.statistics.indexstatistics_test import (
    TestCaseIndexstatistics as Indexstatistics,
)

from testcases.template.templateCreate_test import (
    TestCaseTemplatecreate as Templatecreate,
)

from testcases.handle.handleCreate_test import TestCaseHandlecreate as Handlecreate

from testcases.handle.resolveHandle_test import TestCaseResolvehandle as Resolvehandle

from testcases.statistics.indexstatistics_2_test import (
    TestCaseIndexstatistics2 as Indexstatistics2,
)


class TestCaseProxyBiaoshistatistic(HttpRunner):

    config = (
        Config("创建标识后查看企业首页标识统计")
        .variables(
            **{
                "handle": "$prefix/${get_random_param(100000,1000000,1)}",
                "version": "zjauto${get_random_param(10000,1000000,1)}",
                "account": "${ENV(adminaccount)}",
                "password": "${ENV(adminpassword)}",
                "email": "${get_email()}",
                "mobile": "${get_mobile()}",
                "username": "${get_username()}",
                "entaccount": "$username",
                "entpassword": "${ENV(entpassword)}",
                "prefix": "${ENV(prefix_second)}${get_random_param(1,10000,1)}",
                "personId": "${get_idcardno()}",
            }
        )
        .export(*["prefixauditid", "proxyserverid"])
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
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddrCity",
                    "entInfoSyss_1_sysType",
                    "userId",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_2_deployAddr",
                    "orgAddrCounty",
                    "entInfoSyss_2_deployMode",
                    "legalCrtType",
                    "entInfoSyss_2_sysType",
                    "imgId_b",
                    "legalCrtBackImgRid",
                    "createDate",
                    "entInfoSyss_3_deployAddrCity",
                    "entInfoSyss_2_deployAddrProvince",
                    "updateDate",
                    "entInfoSyss_0_deployAddrCounty",
                    "applyId",
                    "entId",
                    "industryCategory",
                    "entInfoSyss_3_deployMode",
                    "orgCrtCode",
                    "orgCrtType",
                    "orgAddrCity",
                    "entUserId",
                    "orgAddrCountyDesc",
                    "entInfoSyss_1_deployAddr",
                    "contactCrtNo",
                    "orgNature",
                    "legalName",
                    "orgAddrCityDesc",
                    "legalCrtNo",
                    "orgAddrProvince",
                    "entApplyId",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_3_id",
                    "entInfoSyss_1_deployAddrProvince",
                    "imgId",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_0_sysType",
                    "industrySpecific",
                    "legalCrtFrontImgRid",
                    "orgCategorySpecificDesc",
                    "contactName",
                    "entInfoSyss_3_deployAddrProvince",
                    "imgId_f",
                    "entInfoSyss_0_id",
                    "userName",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_entApplyId",
                    "contactCrtType",
                    "entInfoSyss_0_deployMode",
                    "contactEmail",
                    "legalPhone",
                    "contactPhone",
                    "entInfoSyss_1_id",
                    "orgNatureDesc",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_2_deployAddrCity",
                    "orgCrtImgRid",
                    "entInfoSyss_1_deployAddrCounty",
                    "entInfoSyss_3_deployAddr",
                    "legalEmail",
                    "prefix",
                    "legalCrtTypeDesc",
                    "orgName",
                    "orgAddr",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_2_deployAddrCounty",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddrCity",
                    "entInfoSyss_1_sysType",
                    "userId",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_2_deployAddr",
                    "orgAddrCounty",
                    "entInfoSyss_2_deployMode",
                    "legalCrtType",
                    "entInfoSyss_2_sysType",
                    "imgId_b",
                    "legalCrtBackImgRid",
                    "createDate",
                    "entInfoSyss_3_deployAddrCity",
                    "entInfoSyss_2_deployAddrProvince",
                    "updateDate",
                    "entInfoSyss_0_deployAddrCounty",
                    "applyId",
                    "entId",
                    "industryCategory",
                    "entInfoSyss_3_deployMode",
                    "orgCrtCode",
                    "orgCrtType",
                    "orgAddrCity",
                    "entUserId",
                    "orgAddrCountyDesc",
                    "entInfoSyss_1_deployAddr",
                    "contactCrtNo",
                    "orgNature",
                    "legalName",
                    "orgAddrCityDesc",
                    "legalCrtNo",
                    "orgAddrProvince",
                    "entApplyId",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_3_id",
                    "entInfoSyss_1_deployAddrProvince",
                    "imgId",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_0_sysType",
                    "industrySpecific",
                    "legalCrtFrontImgRid",
                    "orgCategorySpecificDesc",
                    "contactName",
                    "entInfoSyss_3_deployAddrProvince",
                    "imgId_f",
                    "entInfoSyss_0_id",
                    "userName",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_entApplyId",
                    "contactCrtType",
                    "entInfoSyss_0_deployMode",
                    "contactEmail",
                    "legalPhone",
                    "contactPhone",
                    "entInfoSyss_1_id",
                    "orgNatureDesc",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_2_deployAddrCity",
                    "orgCrtImgRid",
                    "entInfoSyss_1_deployAddrCounty",
                    "entInfoSyss_3_deployAddr",
                    "legalEmail",
                    "prefix",
                    "legalCrtTypeDesc",
                    "orgName",
                    "orgAddr",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_2_deployAddrCounty",
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
        Step(RunTestCase("企业用户登录").call(LoginEnt).export(*["entSession"])),
        Step(RunTestCase("企业申请托管").call(ProxyApply)),
        Step(RunTestCase("管理员用户登录").call(LoginAdmin).export(*["adminSession"])),
        Step(
            RunTestCase("前缀审核列表查询所申请前缀的id")
            .call(Proxyserverauditlist)
            .export(*["prefixauditid"])
        ),
        Step(RunTestCase("获取托管服务器列表").call(Proxyserverlist).export(*["proxyserverid"])),
        Step(RunTestCase("前缀审核通过").call(Proxyserverprefixaudit)),
        Step(
            RunTestCase("管理员用户首页统计数据")
            .call(Indexstatistics)
            .export(
                *[
                    "resolvnum",
                    "delnum",
                    "identityNum",
                    "entNum",
                    "prefixNum",
                    "applyNum",
                ]
            )
        ),
        Step(RunTestCase("数据模板创建").call(Templatecreate)),
        Step(RunTestCase("标识注册").call(Handlecreate)),
        Step(RunTestCase("门户首页递归解析已创建的标识").call(Resolvehandle)),
        Step(RunTestCase("管理员用户首页统计数据").call(Indexstatistics2)),
    ]


if __name__ == "__main__":
    TestCaseProxyBiaoshistatistic().test_start()