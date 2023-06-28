# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixAlloc/ent-prefix-manage-delete-2.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntPrefixManageDelete2(HttpRunner):

    config = Config("前缀删除").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("前缀删除")
            .post("/api/v3/ent/prefix/manage/delete")
            .with_params(
                **{
                    "delTemplateAll": "$delTemplateAll",
                    "entPrefix": "$pendingPrefixConditionSecond",
                    "transferPrefix": "$transferPrefix",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "Pragma": "no-cache",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
                    "X-HTTP-Method-Override": "delete",
                }
            )
            .with_cookies(**{"SESSION": "$adminSession"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseEntPrefixManageDelete2().test_start()
