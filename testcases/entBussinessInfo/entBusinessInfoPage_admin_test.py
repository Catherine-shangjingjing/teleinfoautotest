# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/entBussinessInfo/entBusinessInfoPage-admin.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntbusinessinfopageAdmin(HttpRunner):

    config = (
        Config("标识业务数据分页列表")
        .variables(**{"currentPage": "1"})
        .base_url("${ENV(HOST)}")
        .verify(False)
        .export(*["entBusinessId"])
    )

    teststeps = [
        Step(
            RunRequest("标识业务数据分页列表")
            .get("/api/v3/entBussInfo/pageQuery")
            .with_params(
                **{
                    "currentPage": "$currentPage",
                    "orgName": "$orgName",
                    "prefix": "$prefix",
                    "appName": "$appName",
                    "appType": "$appType",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$adminSession"})
            .extract()
            .with_jmespath("body.data.content[0].id", "entBusinessId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json;charset=UTF-8")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
        ),
    ]


if __name__ == "__main__":
    TestCaseEntbusinessinfopageAdmin().test_start()
