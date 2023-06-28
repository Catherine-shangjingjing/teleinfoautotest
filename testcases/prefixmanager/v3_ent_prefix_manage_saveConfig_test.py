# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixmanager/v3-ent-prefix-manage-saveConfig.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseV3EntPrefixManageSaveconfig(HttpRunner):

    config = (
        Config("保存前缀配置")
        .variables(**{"entPrefix": "$prefix", "objName": "$prefix"})
        .base_url("${ENV(HOST)}")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("保存前缀配置")
            .post("/api/v3/ent/prefix/manage/saveConfig")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
                }
            )
            .with_cookies(**{"SESSION": "$adminSession"})
            .with_json(
                {
                    "entNameCn": "$entNameCn",
                    "entPrefix": "$prefix",
                    "ip": "$ip",
                    "ipType": "$ipType",
                    "objName": "$prefix",
                    "prefixId": "$prefixId",
                    "tcpPort": "$tcpPort",
                    "userId": "$userId",
                    "httpPort": "$httpPort",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseV3EntPrefixManageSaveconfig().test_start()
