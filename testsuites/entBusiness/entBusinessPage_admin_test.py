# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/entBusiness/entBusinessPage-admin.yaml


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

from testcases.entBussinessInfo.entBusinessInfoAdd_test import (
    TestCaseEntbusinessinfoadd as Entbusinessinfoadd,
)

from testcases.entBussinessInfo.entBusinessInfoPage_admin_test import (
    TestCaseEntbusinessinfopageAdmin as EntbusinessinfopageAdmin,
)


class TestCaseEntbusinesspageAdmin(HttpRunner):

    config = Config("标识业务数据-管理员查看-39").variables(
        **{
            "email": "${get_email()}",
            "mobile": "${get_mobile()}",
            "username": "${get_username()}",
            "account": "${ENV(adminaccount)}",
            "password": "${ENV(adminpassword)}",
            "entaccount": "$username",
            "entpassword": "${ENV(entpassword)}",
            "appDesc": "sdad",
            "appName": "${get_random_param(1,1000000000)}",
            "appRdunit": "bbbbbbbbbbbsdadsdasdasbbbbb",
            "appType": 1,
            "appUserCount": "${get_random_param(1,10000)}",
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
                    "entInfoSyss_0_deployAddrCity",
                    "imgId_f",
                    "orgAddrProvinceDesc",
                    "orgCrtType",
                    "imgId",
                    "createDate",
                    "orgName",
                    "updateDate",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_3_deployAddrCity",
                    "orgAddr",
                    "orgNatureDesc",
                    "entInfoSyss_2_id",
                    "orgNature",
                    "userId",
                    "contactPhone",
                    "entInfoSyss_2_deployAddrProvince",
                    "orgCrtImgRid",
                    "industryCategory",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_2_deployAddrCounty",
                    "legalCrtBackImgRid",
                    "legalCrtType",
                    "entInfoSyss_3_sysType",
                    "legalCrtTypeDesc",
                    "legalPhone",
                    "contactName",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_3_id",
                    "entApplyId",
                    "entId",
                    "orgCrtCode",
                    "legalName",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_1_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddrCityDesc",
                    "legalEmail",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_1_id",
                    "userName",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_3_deployAddr",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_deployMode",
                    "entUserId",
                    "entInfoSyss_1_deployAddrProvince",
                    "orgAddrCountyDesc",
                    "entInfoSyss_2_deployAddr",
                    "prefix",
                    "entInfoSyss_1_deployAddr",
                    "imgId_b",
                    "orgAddrCity",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_2_deployMode",
                    "orgAddrCounty",
                    "legalCrtNo",
                    "contactCrtType",
                    "entInfoSyss_0_id",
                    "industrySpecific",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_0_deployAddr",
                    "applyId",
                    "contactEmail",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_1_deployAddrCounty",
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
                    "entInfoSyss_0_deployAddrCity",
                    "imgId_f",
                    "orgAddrProvinceDesc",
                    "orgCrtType",
                    "imgId",
                    "createDate",
                    "orgName",
                    "updateDate",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_3_deployAddrCity",
                    "orgAddr",
                    "orgNatureDesc",
                    "entInfoSyss_2_id",
                    "orgNature",
                    "userId",
                    "contactPhone",
                    "entInfoSyss_2_deployAddrProvince",
                    "orgCrtImgRid",
                    "industryCategory",
                    "entInfoSyss_1_deployMode",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_2_deployAddrCounty",
                    "legalCrtBackImgRid",
                    "legalCrtType",
                    "entInfoSyss_3_sysType",
                    "legalCrtTypeDesc",
                    "legalPhone",
                    "contactName",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_3_id",
                    "entApplyId",
                    "entId",
                    "orgCrtCode",
                    "legalName",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_1_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddrCityDesc",
                    "legalEmail",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_1_id",
                    "userName",
                    "legalCrtFrontImgRid",
                    "entInfoSyss_3_deployAddr",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_deployMode",
                    "entUserId",
                    "entInfoSyss_1_deployAddrProvince",
                    "orgAddrCountyDesc",
                    "entInfoSyss_2_deployAddr",
                    "prefix",
                    "entInfoSyss_1_deployAddr",
                    "imgId_b",
                    "orgAddrCity",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_2_deployMode",
                    "orgAddrCounty",
                    "legalCrtNo",
                    "contactCrtType",
                    "entInfoSyss_0_id",
                    "industrySpecific",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_0_deployAddr",
                    "applyId",
                    "contactEmail",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_1_deployAddrCounty",
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
        Step(RunTestCase("登录-企业").call(LoginEnt).export(*["entSession"])),
        Step(RunTestCase("添加标识业务数据").call(Entbusinessinfoadd)),
        Step(RunTestCase("登录-管理员").call(LoginAdmin).export(*["adminSession"])),
        Step(
            RunTestCase("查看标识业务列表")
            .call(EntbusinessinfopageAdmin)
            .export(*["entBusinessId"])
        ),
    ]


if __name__ == "__main__":
    TestCaseEntbusinesspageAdmin().test_start()