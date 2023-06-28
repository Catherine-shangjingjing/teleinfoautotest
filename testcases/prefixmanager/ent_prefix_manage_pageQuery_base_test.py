# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixmanager/ent-prefix-manage-pageQuery-base.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntPrefixManagePagequeryBase(HttpRunner):

    config = (
        Config("前缀管理分页")
        .base_url("${ENV(HOST)}")
        .verify(False)
        .export(
            *[
                "entNameCnPage",
                "entPrefixPage",
                "prefixIdPage",
                "userIdPage",
                "proxyStatePage",
            ]
        )
    )

    teststeps = [
        Step(
            RunRequest("前缀管理分页")
            .get("/api/v3/ent/prefix/manage/pageQuery")
            .with_params(
                **{
                    "cache": "1663838231980",
                    "currentPage": "1",
                    "entPrefix": "$prefix",
                    "escrowOrgName": "",
                    "order": "",
                    "orderProp": "",
                }
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
            .with_jmespath("body.data.content[0].userId", "userIdPage")
            .with_jmespath("body.data.content[0].entPrefix", "entPrefixPage")
            .with_jmespath("body.data.content[0].id", "prefixIdPage")
            .with_jmespath("body.data.content[0].entName", "entNameCnPage")
            .with_jmespath("body.data.content[0].proxyState", "proxyStatePage")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseEntPrefixManagePagequeryBase().test_start()
