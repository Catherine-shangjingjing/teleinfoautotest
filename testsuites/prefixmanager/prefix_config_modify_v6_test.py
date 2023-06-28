# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/prefixmanager/prefix_config_modify_v6.yml


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

from testcases.prefixmanager.ent_prefix_manage_pageQuery_config_test import (
    TestCaseEntPrefixManagePagequeryConfig as EntPrefixManagePagequeryConfig,
)

from testcases.prefixmanager.ent_prefix_manage_saveConfig_test import (
    TestCaseEntPrefixManageSaveconfig as EntPrefixManageSaveconfig,
)

from testcases.prefixmanager.ent_prefix_manage_configPage_test import (
    TestCaseEntPrefixManageConfigpage as EntPrefixManageConfigpage,
)

from testcases.prefixmanager.ent_prefix_manage_saveConfig_modify_test import (
    TestCaseEntPrefixManageSaveconfigModify as EntPrefixManageSaveconfigModify,
)

from testcases.prefixmanager.ent_prefix_manage_configPage_modify_test import (
    TestCaseEntPrefixManageConfigpageModify as EntPrefixManageConfigpageModify,
)

from testcases.logmanager.log_operation_pageQuery_test import (
    TestCaseLogOperationPagequery as LogOperationPagequery,
)


class TestCasePrefixConfigModifyV6(HttpRunner):

    config = Config("前缀配置-修改-v6").variables(
        **{
            "email": "${get_email()}",
            "mobile": "${get_mobile()}",
            "username": "${get_username()}",
            "account": "${ENV(adminaccount)}",
            "password": "${ENV(adminpassword)}",
            "entaccount": "$username",
            "entpassword": "${ENV(entpassword)}",
            "ip": "${get_random_ipv6()}",
            "ipType": 6,
            "tcpPort": "${get_random_port()}",
            "httpPort": "${get_random_port()}",
            "udpPort": "${get_random_port()}",
            "modifyIp": "${get_random_ipv6()}",
            "modifyIpType": 6,
            "modifyTcpPort": "${get_random_port()}",
            "modifyHttpPort": "${get_random_port()}",
            "modifyUdpPort": "${get_random_port()}",
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
                    "orgNature",
                    "entInfoSyss_1_deployAddrProvince",
                    "updateDate",
                    "entInfoSyss_0_id",
                    "entInfoSyss_0_deployAddrCity",
                    "legalName",
                    "orgAddrCountyDesc",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_2_deployAddrCounty",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_0_deployAddrCounty",
                    "userId",
                    "imgId",
                    "orgCrtCode",
                    "legalCrtType",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_2_deployAddr",
                    "imgId_b",
                    "orgAddrCityDesc",
                    "prefix",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_2_id",
                    "entInfoSyss_3_sysType",
                    "contactPhone",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddr",
                    "entInfoSyss_1_id",
                    "entInfoSyss_0_deployMode",
                    "entApplyId",
                    "legalCrtTypeDesc",
                    "legalCrtNo",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_2_sysType",
                    "orgCrtImgRid",
                    "legalPhone",
                    "orgAddrCounty",
                    "applyId",
                    "entInfoSyss_3_deployAddrCounty",
                    "orgAddr",
                    "entInfoSyss_3_id",
                    "entInfoSyss_3_deployAddrCity",
                    "orgNatureDesc",
                    "entUserId",
                    "contactCrtType",
                    "entInfoSyss_2_deployMode",
                    "contactEmail",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddrCity",
                    "entInfoSyss_3_entApplyId",
                    "userName",
                    "entInfoSyss_1_deployAddrCity",
                    "orgName",
                    "entInfoSyss_2_deployAddrProvince",
                    "contactCrtNo",
                    "entInfoSyss_3_deployAddr",
                    "legalEmail",
                    "entInfoSyss_0_sysType",
                    "orgAddrProvince",
                    "legalCrtFrontImgRid",
                    "orgCrtType",
                    "legalCrtBackImgRid",
                    "contactName",
                    "industryCategory",
                    "entId",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_1_deployAddrCounty",
                    "industrySpecific",
                    "imgId_f",
                    "createDate",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "orgNature",
                    "entInfoSyss_1_deployAddrProvince",
                    "updateDate",
                    "entInfoSyss_0_id",
                    "entInfoSyss_0_deployAddrCity",
                    "legalName",
                    "orgAddrCountyDesc",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_2_deployAddrCounty",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_0_deployAddrCounty",
                    "userId",
                    "imgId",
                    "orgCrtCode",
                    "legalCrtType",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_2_deployAddr",
                    "imgId_b",
                    "orgAddrCityDesc",
                    "prefix",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_2_id",
                    "entInfoSyss_3_sysType",
                    "contactPhone",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_deployAddr",
                    "entInfoSyss_1_id",
                    "entInfoSyss_0_deployMode",
                    "entApplyId",
                    "legalCrtTypeDesc",
                    "legalCrtNo",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_2_sysType",
                    "orgCrtImgRid",
                    "legalPhone",
                    "orgAddrCounty",
                    "applyId",
                    "entInfoSyss_3_deployAddrCounty",
                    "orgAddr",
                    "entInfoSyss_3_id",
                    "entInfoSyss_3_deployAddrCity",
                    "orgNatureDesc",
                    "entUserId",
                    "contactCrtType",
                    "entInfoSyss_2_deployMode",
                    "contactEmail",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddrCity",
                    "entInfoSyss_3_entApplyId",
                    "userName",
                    "entInfoSyss_1_deployAddrCity",
                    "orgName",
                    "entInfoSyss_2_deployAddrProvince",
                    "contactCrtNo",
                    "entInfoSyss_3_deployAddr",
                    "legalEmail",
                    "entInfoSyss_0_sysType",
                    "orgAddrProvince",
                    "legalCrtFrontImgRid",
                    "orgCrtType",
                    "legalCrtBackImgRid",
                    "contactName",
                    "industryCategory",
                    "entId",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_1_deployAddrCounty",
                    "industrySpecific",
                    "imgId_f",
                    "createDate",
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
        Step(
            RunTestCase("前缀管理分页")
            .call(EntPrefixManagePagequeryConfig)
            .export(
                *[
                    "entNameCnPage",
                    "proxyStatePage",
                    "userIdPage",
                    "entPrefixPage",
                    "prefixIdPage",
                ]
            )
        ),
        Step(RunTestCase("前缀配置保存V6").call(EntPrefixManageSaveconfig)),
        Step(RunTestCase("配置分页").call(EntPrefixManageConfigpage).export(*["configId"])),
        Step(
            RunTestCase("前缀管理分页")
            .call(EntPrefixManagePagequeryConfig)
            .export(
                *[
                    "entNameCnPage",
                    "proxyStatePage",
                    "userIdPage",
                    "entPrefixPage",
                    "prefixIdPage",
                ]
            )
        ),
        Step(RunTestCase("前缀配置修改V6").call(EntPrefixManageSaveconfigModify)),
        Step(RunTestCase("修改配置分页").call(EntPrefixManageConfigpageModify)),
        Step(RunTestCase("操作日志列表").call(LogOperationPagequery)),
    ]


if __name__ == "__main__":
    TestCasePrefixConfigModifyV6().test_start()