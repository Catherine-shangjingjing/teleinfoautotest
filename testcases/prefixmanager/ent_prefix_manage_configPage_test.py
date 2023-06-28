# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixmanager/ent-prefix-manage-configPage.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntPrefixManageConfigpage(HttpRunner):

    config = (
        Config("前缀管理-配置分页").base_url("${ENV(HOST)}").verify(False).export(*["configId"])
    )

    teststeps = [
        Step(
            RunRequest("前缀管理-配置分页")
            .get("/api/v3/ent/prefix/manage/configPage")
            .with_params(
                **{"entPrefix": "$pendingPrefixCondition", "userId": "$userIdPage"}
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
                }
            )
            .with_cookies(**{"SESSION": "$adminSession"})
            .extract()
            .with_jmespath(
                "body.data.nbmsEntPrefixPOs[1].prefixConfigPO[0].id", "configId"
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data.nbmsEntPrefixPOs[1].prefixConfigPO[0].ip", "$ip")
            .assert_equal(
                "body.data.nbmsEntPrefixPOs[1].prefixConfigPO[0].httpPort", "$httpPort"
            )
            .assert_equal(
                "body.data.nbmsEntPrefixPOs[1].prefixConfigPO[0].udpPort", "$udpPort"
            )
            .assert_equal(
                "body.data.nbmsEntPrefixPOs[1].prefixConfigPO[0].tcpPort", "$tcpPort"
            )
        ),
    ]


if __name__ == "__main__":
    TestCaseEntPrefixManageConfigpage().test_start()
