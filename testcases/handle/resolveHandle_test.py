# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/handle/resolveHandle.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseResolvehandle(HttpRunner):

    config = Config("门户页解析").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("门户页解析")
            .setup_hook("${hook_example()}")
            .get("/api/identityv2/query/data")
            .with_params(**{"handle": "$handle"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_contains("body.data.handleVO.value[6].value", "新增属性中文测试")
            .assert_contains(
                "body.data.handleVO.value[0].value", "2125654564tryrt混合类型JLHLH"
            )
        ),
    ]


if __name__ == "__main__":
    TestCaseResolvehandle().test_start()
