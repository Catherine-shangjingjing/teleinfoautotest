# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/template/templateUpload.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTemplateupload(HttpRunner):

    config = Config("数据模板申报").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("数据模板申报")
            .get("/api/v5/identity/template/templateUpload")
            .with_params(**{"cache": "1663838246176", "templateId": "${template_id}"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$entSession"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.message", "成功")
            .assert_equal("body.status", 1)
            .assert_equal("body.data", None)
        ),
    ]


if __name__ == "__main__":
    TestCaseTemplateupload().test_start()
