# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/applyRecord/entApply-ent.yml


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

from testcases.applyRecord.entApplyRecordPage_ent_test import (
    TestCaseEntapplyrecordpageEnt as EntapplyrecordpageEnt,
)

from testcases.applyRecord.applyrecorddetail_ent_test import (
    TestCaseApplyrecorddetailEnt as ApplyrecorddetailEnt,
)


class TestCaseEntapplyEnt(HttpRunner):

    config = Config("申请记录分页-ent-35,36").variables(
        **{
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
                    "applyId",
                    "orgNatureDesc",
                    "entInfoSyss_2_entApplyId",
                    "orgAddrCounty",
                    "orgAddr",
                    "entInfoSyss_1_deployAddr",
                    "orgCategorySpecificDesc",
                    "imgId_f",
                    "orgAddrCity",
                    "contactName",
                    "industrySpecific",
                    "entInfoSyss_2_id",
                    "orgCrtType",
                    "userId",
                    "contactCrtNo",
                    "legalCrtFrontImgRid",
                    "legalCrtBackImgRid",
                    "entInfoSyss_1_id",
                    "entInfoSyss_3_id",
                    "legalCrtTypeDesc",
                    "updateDate",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_1_deployAddrCounty",
                    "contactCrtType",
                    "createDate",
                    "orgCrtCode",
                    "legalCrtNo",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_0_deployAddr",
                    "orgName",
                    "entInfoSyss_1_deployMode",
                    "entApplyId",
                    "entInfoSyss_2_deployAddrCounty",
                    "entInfoSyss_3_deployAddrCity",
                    "legalCrtType",
                    "entId",
                    "contactEmail",
                    "userName",
                    "prefix",
                    "legalEmail",
                    "orgNature",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_3_deployAddr",
                    "orgAddrCityDesc",
                    "contactPhone",
                    "imgId",
                    "industryCategory",
                    "orgCrtImgRid",
                    "orgAddrCountyDesc",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "legalPhone",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_0_id",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_3_entApplyId",
                    "entUserId",
                    "entInfoSyss_2_deployAddrProvince",
                    "legalName",
                    "entInfoSyss_0_deployAddrCity",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_1_deployAddrCity",
                    "imgId_b",
                    "entInfoSyss_3_sysType",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "applyId",
                    "orgNatureDesc",
                    "entInfoSyss_2_entApplyId",
                    "orgAddrCounty",
                    "orgAddr",
                    "entInfoSyss_1_deployAddr",
                    "orgCategorySpecificDesc",
                    "imgId_f",
                    "orgAddrCity",
                    "contactName",
                    "industrySpecific",
                    "entInfoSyss_2_id",
                    "orgCrtType",
                    "userId",
                    "contactCrtNo",
                    "legalCrtFrontImgRid",
                    "legalCrtBackImgRid",
                    "entInfoSyss_1_id",
                    "entInfoSyss_3_id",
                    "legalCrtTypeDesc",
                    "updateDate",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_3_deployAddrProvince",
                    "entInfoSyss_1_deployAddrCounty",
                    "contactCrtType",
                    "createDate",
                    "orgCrtCode",
                    "legalCrtNo",
                    "entInfoSyss_3_deployMode",
                    "entInfoSyss_1_deployAddrProvince",
                    "entInfoSyss_3_deployAddrCounty",
                    "entInfoSyss_1_sysType",
                    "entInfoSyss_0_deployAddr",
                    "orgName",
                    "entInfoSyss_1_deployMode",
                    "entApplyId",
                    "entInfoSyss_2_deployAddrCounty",
                    "entInfoSyss_3_deployAddrCity",
                    "legalCrtType",
                    "entId",
                    "contactEmail",
                    "userName",
                    "prefix",
                    "legalEmail",
                    "orgNature",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_3_deployAddr",
                    "orgAddrCityDesc",
                    "contactPhone",
                    "imgId",
                    "industryCategory",
                    "orgCrtImgRid",
                    "orgAddrCountyDesc",
                    "entInfoSyss_0_entApplyId",
                    "entInfoSyss_0_deployAddrCounty",
                    "legalPhone",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_0_id",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddrProvince",
                    "entInfoSyss_3_entApplyId",
                    "entUserId",
                    "entInfoSyss_2_deployAddrProvince",
                    "legalName",
                    "entInfoSyss_0_deployAddrCity",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_2_deployMode",
                    "entInfoSyss_1_deployAddrCity",
                    "imgId_b",
                    "entInfoSyss_3_sysType",
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
            RunTestCase("申请记录分页-ent").call(EntapplyrecordpageEnt).export(*["applyId"])
        ),
        Step(RunTestCase("申请记录详情-ent").call(ApplyrecorddetailEnt)),
    ]


if __name__ == "__main__":
    TestCaseEntapplyEnt().test_start()
