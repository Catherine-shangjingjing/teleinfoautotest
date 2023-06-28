# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/checkFlow/check_prefix_fail.yml


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

from testcases.verification.ent_apply_verification_legalQualify_test import (
    TestCaseEntApplyVerificationLegalqualify as EntApplyVerificationLegalqualify,
)

from testcases.logmanager.verficationlog_test import (
    TestCaseVerficationlog as Verficationlog,
)

from testcases.verification.ent_apply_verification_legalIdentify_test import (
    TestCaseEntApplyVerificationLegalidentify as EntApplyVerificationLegalidentify,
)

from testcases.logmanager.verficationlog1_test import (
    TestCaseVerficationlog1 as Verficationlog1,
)

from testcases.verification.ent_apply_verification_contactIdentify_test import (
    TestCaseEntApplyVerificationContactidentify as EntApplyVerificationContactidentify,
)

from testcases.logmanager.verficationlog2_test import (
    TestCaseVerficationlog2 as Verficationlog2,
)


class TestCaseCheckPrefixFail(HttpRunner):

    config = (
        Config("核验接口")
        .variables(
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
        .base_url("${ENV(HOST)}")
        .verify(False)
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
                    "entInfoSyss_1_deployAddr",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_1_deployAddrCounty",
                    "orgNatureDesc",
                    "legalCrtFrontImgRid",
                    "applyId",
                    "orgNature",
                    "entInfoSyss_3_deployAddrProvince",
                    "entId",
                    "entInfoSyss_3_entApplyId",
                    "contactName",
                    "orgAddrCountyDesc",
                    "industryCategory",
                    "prefix",
                    "entInfoSyss_2_deployAddrCounty",
                    "orgAddrCounty",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_entApplyId",
                    "orgAddrCity",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_2_deployMode",
                    "legalPhone",
                    "entInfoSyss_1_deployMode",
                    "orgCrtImgRid",
                    "entInfoSyss_1_deployAddrProvince",
                    "industrySpecific",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_2_deployAddr",
                    "orgAddrCityDesc",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_1_deployAddrCity",
                    "legalCrtBackImgRid",
                    "entInfoSyss_2_entApplyId",
                    "orgCrtCode",
                    "entInfoSyss_3_deployAddrCity",
                    "imgId_b",
                    "imgId",
                    "legalCrtNo",
                    "entInfoSyss_3_sysType",
                    "userName",
                    "entInfoSyss_3_id",
                    "entInfoSyss_2_deployAddrProvince",
                    "createDate",
                    "userId",
                    "orgAddrProvince",
                    "orgCrtType",
                    "entInfoSyss_3_deployAddrCounty",
                    "contactCrtNo",
                    "entInfoSyss_1_sysType",
                    "orgName",
                    "updateDate",
                    "entApplyId",
                    "entInfoSyss_0_id",
                    "entInfoSyss_0_deployMode",
                    "entUserId",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddr",
                    "legalEmail",
                    "contactPhone",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_2_id",
                    "imgId_f",
                    "legalName",
                    "legalCrtType",
                    "legalCrtTypeDesc",
                    "entInfoSyss_1_id",
                    "entInfoSyss_3_deployAddr",
                    "entInfoSyss_3_deployMode",
                    "contactEmail",
                    "contactCrtType",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "entInfoSyss_1_deployAddr",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_0_deployAddrCounty",
                    "entInfoSyss_1_deployAddrCounty",
                    "orgNatureDesc",
                    "legalCrtFrontImgRid",
                    "applyId",
                    "orgNature",
                    "entInfoSyss_3_deployAddrProvince",
                    "entId",
                    "entInfoSyss_3_entApplyId",
                    "contactName",
                    "orgAddrCountyDesc",
                    "industryCategory",
                    "prefix",
                    "entInfoSyss_2_deployAddrCounty",
                    "orgAddrCounty",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_0_entApplyId",
                    "orgAddrCity",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_2_deployMode",
                    "legalPhone",
                    "entInfoSyss_1_deployMode",
                    "orgCrtImgRid",
                    "entInfoSyss_1_deployAddrProvince",
                    "industrySpecific",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_2_deployAddr",
                    "orgAddrCityDesc",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_1_deployAddrCity",
                    "legalCrtBackImgRid",
                    "entInfoSyss_2_entApplyId",
                    "orgCrtCode",
                    "entInfoSyss_3_deployAddrCity",
                    "imgId_b",
                    "imgId",
                    "legalCrtNo",
                    "entInfoSyss_3_sysType",
                    "userName",
                    "entInfoSyss_3_id",
                    "entInfoSyss_2_deployAddrProvince",
                    "createDate",
                    "userId",
                    "orgAddrProvince",
                    "orgCrtType",
                    "entInfoSyss_3_deployAddrCounty",
                    "contactCrtNo",
                    "entInfoSyss_1_sysType",
                    "orgName",
                    "updateDate",
                    "entApplyId",
                    "entInfoSyss_0_id",
                    "entInfoSyss_0_deployMode",
                    "entUserId",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_2_deployAddrCity",
                    "orgAddr",
                    "legalEmail",
                    "contactPhone",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_2_sysType",
                    "entInfoSyss_2_id",
                    "imgId_f",
                    "legalName",
                    "legalCrtType",
                    "legalCrtTypeDesc",
                    "entInfoSyss_1_id",
                    "entInfoSyss_3_deployAddr",
                    "entInfoSyss_3_deployMode",
                    "contactEmail",
                    "contactCrtType",
                ]
            )
        ),
        Step(RunTestCase("企业注册最终第三步提交信息").call(SubmitFinal)),
        Step(RunTestCase("登录-管理员").call(LoginAdmin).export(*["adminSession"])),
        Step(RunTestCase("法人资格核验接口").call(EntApplyVerificationLegalqualify)),
        Step(RunTestCase("核验日志列表").call(Verficationlog)),
        Step(RunTestCase("法人身份核验接口").call(EntApplyVerificationLegalidentify)),
        Step(RunTestCase("核验日志列表").call(Verficationlog1)),
        Step(RunTestCase("联系人身份核验接口").call(EntApplyVerificationContactidentify)),
        Step(RunTestCase("核验日志列表").call(Verficationlog2)),
    ]


if __name__ == "__main__":
    TestCaseCheckPrefixFail().test_start()
