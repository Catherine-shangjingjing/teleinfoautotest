# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/entdetail/ent-detail.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseEntDetail(HttpRunner):

    config = Config("企业信息详情").base_url("${ENV(HOST)}").verify(False).export(*["entId"])

    teststeps = [
        Step(
            RunRequest("企业信息详情")
            .get("/api/v3/ent/detail")
            .with_params(**{"isSensetive": "1", "userId": "$userId"})
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
            .with_jmespath("body.data.nbmsEntPO.id", "entId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
        ),
    ]


if __name__ == "__main__":
    TestCaseEntDetail().test_start()
