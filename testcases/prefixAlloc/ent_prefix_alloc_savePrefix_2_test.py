# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixAlloc/ent-prefix-alloc-savePrefix-2.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntPrefixAllocSaveprefix2(HttpRunner):

    config = Config("保存再分配的前缀").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("保存再分配的前缀")
            .post("/api/v3/ent/prefix/alloc/savePrefix")
            .with_params(
                **{
                    "annualFeeRuleId": "$annualFeeRuleId",
                    "pendingPrefix": "$pendingPrefixConditionSecond",
                    "regFeeRuleId": "$regFeeRuleId",
                    "userId": "$userId",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
                }
            )
            .with_cookies(**{"SESSION": "$adminSession"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data", "分配完成")
        ),
    ]


if __name__ == "__main__":
    TestCaseEntPrefixAllocSaveprefix2().test_start()
