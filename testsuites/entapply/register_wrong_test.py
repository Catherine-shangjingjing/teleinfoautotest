# NOTE: Generated By HttpRunner v3.1.6
# FROM: testsuites/entapply/register_wrong.yml


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

from testcases.prefixAudit.register.submit_wrong_test import (
    TestCaseSubmitWrong as SubmitWrong,
)


class TestCaseRegisterWrong(HttpRunner):

    config = Config("企业注册信息用例集").variables(
        **{
            "username": "${get_username()}",
            "entaccount": "$username",
            "entpassword": "${ENV(entpassword)}",
            "email": "${get_email()}",
            "mobile": "${get_mobile()}",
            "account": "${ENV(adminaccount)}",
            "password": "${ENV(adminpassword)}",
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
        Step(RunTestCase("企业注册第一步提交信息").call(SubmitWrong)),
    ]


if __name__ == "__main__":
    TestCaseRegisterWrong().test_start()
