# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/login/login-ent.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginEnt(HttpRunner):

    config = (
        Config("登录-企业用户").base_url("${ENV(HOST)}").verify(False).export(*["entSession"])
    )

    teststeps = [
        Step(
            RunRequest("登录-企业用户")
            .post("/api/home/test/login")
            .with_headers(
                **{
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Content-Length": "204",
                    "Content-Type": "application/json",
                    "User-Agent": "python-requests/2.28.1",
                }
            )
            .with_json(
                {
                    "captcha": "0000",
                    "captchaSign": "${get_captcha_sign($entaccount, $entpassword)}",
                    "emailCaptcha": "",
                    "username": "$entaccount",
                }
            )
            .extract()
            .with_jmespath('response.headers."Set-Cookie".session', "entSession")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginEnt().test_start()
