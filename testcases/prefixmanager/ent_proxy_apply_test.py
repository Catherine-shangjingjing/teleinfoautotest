# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixmanager/ent-proxy-apply.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntProxyApply(HttpRunner):

    config = Config("企业托管申请").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("托管申请")
            .get("/api/prefixProxy/apply")
            .with_params(**{"entPrefix": "$pendingPrefixCondition"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$entSession"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseEntProxyApply().test_start()