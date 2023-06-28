# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/logmanager/userlog.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseUserlog(HttpRunner):

    config = Config("用户日志列表").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("用户日志列表")
            .get("/api/log/snms/user")
            .with_params(
                **{
                    "cache": "1663914572123",
                    "currentPage": "1",
                    "order": "",
                    "orderProp": "",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$adminSession"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data.content[0].content", "登录成功")
            .assert_equal("body.data.content[0].operationName", "$account")
            .assert_equal("body.data.content[0].operationType", 4)
        ),
    ]


if __name__ == "__main__":
    TestCaseUserlog().test_start()