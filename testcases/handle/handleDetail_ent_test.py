# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/handle/handleDetail-ent.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseHandledetailEnt(HttpRunner):

    config = Config("标识详情").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("标识详情")
            .get("/api/snms/identityv2/data/detail")
            .with_params(
                **{"cache": "1663841946863", "handle": "$handle", "version": "$version"}
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
            .with_cookies(**{"SESSION": "$entSession"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_contains("body.data.value[0].name", "终端类型")
            .assert_contains(
                "body.data.value[0].data.value", "2125654564tryrt混合类型JLHLH"
            )
            .assert_contains("body.data.value[6].data.value", "新增属性中文测试")
        ),
    ]


if __name__ == "__main__":
    TestCaseHandledetailEnt().test_start()