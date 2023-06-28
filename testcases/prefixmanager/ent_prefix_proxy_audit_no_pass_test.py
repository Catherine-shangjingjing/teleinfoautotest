# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixmanager/ent-prefix-proxy-audit-no-pass.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntPrefixProxyAuditNoPass(HttpRunner):

    config = Config("托管审核保存").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("托管审核保存")
            .post("/api/proxyserver/prefix/audit/save")
            .with_params(
                **{
                    "auditResult": "fail",
                    "id": "$prefixauditid",
                    "ids": "$proxyServerId",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$adminSession"})
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseEntPrefixProxyAuditNoPass().test_start()
