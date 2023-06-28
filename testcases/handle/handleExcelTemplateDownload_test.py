# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/handle/handleExcelTemplateDownload.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseHandleexceltemplatedownload(HttpRunner):

    config = Config("标识excel模版下载").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("标识excel模版下载")
            .get("/api/identityv2/template/download/excel")
            .with_params(**{"id": "$template_id"})
            .with_headers(
                **{
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$entSession"})
            .teardown_hook("${hook_down($response)}")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"',
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        ),
    ]


if __name__ == "__main__":
    TestCaseHandleexceltemplatedownload().test_start()