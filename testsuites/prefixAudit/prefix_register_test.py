# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/prefixAudit/prefix_register.yml


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


class TestCasePrefixRegister(HttpRunner):

    config = Config("前缀注册提交成功").variables(
        **{
            "email": "${get_email()}",
            "mobile": "${get_mobile()}",
            "username": "${get_username()}",
            "account": "${ENV(adminaccount)}",
            "password": "${ENV(adminpassword)}",
            "entaccount": "$username",
            "entpassword": "${ENV(entpassword)}",
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
                    "entInfoSyss_0_id",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_3_deployAddrCounty",
                    "legalCrtType",
                    "applyId",
                    "orgAddrProvince",
                    "legalCrtFrontImgRid",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_2_deployAddrCity",
                    "entInfoSyss_3_deployAddr",
                    "legalCrtBackImgRid",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_1_deployMode",
                    "userId",
                    "industryCategory",
                    "prefix",
                    "orgCrtCode",
                    "orgAddr",
                    "entInfoSyss_3_id",
                    "imgId_f",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_1_deployAddrCity",
                    "legalName",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_2_deployAddrProvince",
                    "updateDate",
                    "entInfoSyss_0_deployAddrCounty",
                    "contactCrtType",
                    "entUserId",
                    "legalEmail",
                    "entInfoSyss_2_sysType",
                    "orgAddrCityDesc",
                    "entApplyId",
                    "entId",
                    "legalPhone",
                    "imgId",
                    "contactPhone",
                    "entInfoSyss_2_deployMode",
                    "contactCrtNo",
                    "legalCrtNo",
                    "entInfoSyss_2_deployAddrCounty",
                    "userName",
                    "orgAddrCountyDesc",
                    "contactEmail",
                    "entInfoSyss_1_deployAddr",
                    "contactName",
                    "imgId_b",
                    "orgAddrCounty",
                    "legalCrtTypeDesc",
                    "createDate",
                    "entInfoSyss_3_deployAddrProvince",
                    "orgCrtImgRid",
                    "orgNatureDesc",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_3_deployMode",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_1_deployAddrCounty",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_deployAddrProvince",
                    "industrySpecific",
                    "orgNature",
                    "entInfoSyss_1_id",
                    "orgAddrCity",
                    "entInfoSyss_3_deployAddrCity",
                    "entInfoSyss_1_sysType",
                    "orgName",
                    "orgCrtType",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_0_entApplyId",
                ]
            )
        ),
        Step(RunTestCase("企业注册第二步提交信息").call(SubmitSecond)),
        Step(
            RunTestCase("企业注册查询注册信息")
            .call(ApplyOrNot)
            .export(
                *[
                    "entInfoSyss_0_id",
                    "entInfoSyss_2_deployAddr",
                    "entInfoSyss_3_deployAddrCounty",
                    "legalCrtType",
                    "applyId",
                    "orgAddrProvince",
                    "legalCrtFrontImgRid",
                    "orgCategorySpecificDesc",
                    "entInfoSyss_2_deployAddrCity",
                    "entInfoSyss_3_deployAddr",
                    "legalCrtBackImgRid",
                    "entInfoSyss_0_deployMode",
                    "entInfoSyss_1_deployMode",
                    "userId",
                    "industryCategory",
                    "prefix",
                    "orgCrtCode",
                    "orgAddr",
                    "entInfoSyss_3_id",
                    "imgId_f",
                    "entInfoSyss_0_deployAddrCity",
                    "entInfoSyss_0_sysType",
                    "entInfoSyss_1_deployAddrCity",
                    "legalName",
                    "entInfoSyss_2_entApplyId",
                    "entInfoSyss_2_deployAddrProvince",
                    "updateDate",
                    "entInfoSyss_0_deployAddrCounty",
                    "contactCrtType",
                    "entUserId",
                    "legalEmail",
                    "entInfoSyss_2_sysType",
                    "orgAddrCityDesc",
                    "entApplyId",
                    "entId",
                    "legalPhone",
                    "imgId",
                    "contactPhone",
                    "entInfoSyss_2_deployMode",
                    "contactCrtNo",
                    "legalCrtNo",
                    "entInfoSyss_2_deployAddrCounty",
                    "userName",
                    "orgAddrCountyDesc",
                    "contactEmail",
                    "entInfoSyss_1_deployAddr",
                    "contactName",
                    "imgId_b",
                    "orgAddrCounty",
                    "legalCrtTypeDesc",
                    "createDate",
                    "entInfoSyss_3_deployAddrProvince",
                    "orgCrtImgRid",
                    "orgNatureDesc",
                    "entInfoSyss_1_entApplyId",
                    "entInfoSyss_3_deployMode",
                    "orgAddrProvinceDesc",
                    "entInfoSyss_3_entApplyId",
                    "entInfoSyss_3_sysType",
                    "entInfoSyss_1_deployAddrCounty",
                    "entInfoSyss_0_deployAddrProvince",
                    "entInfoSyss_2_id",
                    "entInfoSyss_1_deployAddrProvince",
                    "industrySpecific",
                    "orgNature",
                    "entInfoSyss_1_id",
                    "orgAddrCity",
                    "entInfoSyss_3_deployAddrCity",
                    "entInfoSyss_1_sysType",
                    "orgName",
                    "orgCrtType",
                    "entInfoSyss_0_deployAddr",
                    "entInfoSyss_0_entApplyId",
                ]
            )
        ),
        Step(RunTestCase("企业注册最终第三步提交信息").call(SubmitFinal)),
    ]


if __name__ == "__main__":
    TestCasePrefixRegister().test_start()
