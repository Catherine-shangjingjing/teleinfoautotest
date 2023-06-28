# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/handle/handleUpdate-ent.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseHandleupdateEnt(HttpRunner):

    config = (
        Config("标识修改")
        .variables(**{"templateIsExists": True})
        .base_url("${ENV(HOST)}")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("/api/snms/identityv2/data")
            .setup_hook("${setup_hook_example20()}")
            .post("/api/snms/identityv2/data")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Length": "2265",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                    "X-HTTP-Method-Override": "put",
                }
            )
            .with_cookies(**{"SESSION": "$entSession"})
            .with_json(
                {
                    "handle": "$handle",
                    "prefix": "$prefix",
                    "templateIsExists": "$templateIsExists",
                    "templateVersion": "$version",
                    "value": [
                        {
                            "data": {
                                "format": "string",
                                "value": "2125654564tryrt混合类型JLHLH",
                            },
                            "index": 2000,
                            "name": "终端类型",
                            "rules": {"max": 65536, "min": 0, "required": False},
                            "type": "terminalType",
                            "webRule": [
                                {"max": 65536, "message": "最大长度为65536位"},
                                {"message": "最小长度为0位", "min": 0, "trigger": "blur"},
                                {"trigger": "blur"},
                            ],
                        },
                        {
                            "data": {"format": "string", "value": "测试标识注册修改"},
                            "index": 2001,
                            "name": "所属主体",
                            "rules": {"max": 65536, "min": 0, "required": False},
                            "type": "subject",
                            "webRule": [
                                {"max": 65536, "message": "最大长度为65536位"},
                                {"message": "最小长度为0位", "min": 0, "trigger": "blur"},
                                {"trigger": "blur"},
                            ],
                        },
                        {
                            "data": {"format": "string", "value": "测试用途"},
                            "index": 2002,
                            "name": "用途",
                            "rules": {"max": 65536, "min": 0, "required": False},
                            "type": "useFor",
                            "webRule": [
                                {"max": 65536, "message": "最大长度为65536位"},
                                {"message": "最小长度为0位", "min": 0, "trigger": "blur"},
                                {"trigger": "blur"},
                            ],
                        },
                        {
                            "data": {"format": "string", "value": "dfjsldjfslfjls字符测试"},
                            "index": 2003,
                            "name": "串号或IMEI",
                            "rules": {"max": 65536, "min": 0, "required": False},
                            "type": "serOrImei",
                            "webRule": [
                                {"max": 65536, "message": "最大长度为65536位"},
                                {"message": "最小长度为0位", "min": 0, "trigger": "blur"},
                                {"trigger": "blur"},
                            ],
                        },
                        {
                            "data": {"format": "string", "value": "中文测试中文测试"},
                            "index": 2004,
                            "name": "进网许可证编号",
                            "rules": {"max": 65536, "min": 0, "required": False},
                            "type": "licenseNo",
                            "webRule": [
                                {"max": 65536, "message": "最大长度为65536位"},
                                {"message": "最小长度为0位", "min": 0, "trigger": "blur"},
                                {"trigger": "blur"},
                            ],
                        },
                        {
                            "data": {"format": "string", "value": "2408080数字测试"},
                            "index": 2005,
                            "name": "进网许可标志序号",
                            "rules": {"max": 65536, "min": 0, "required": False},
                            "type": "licenseSign",
                            "webRule": [
                                {"max": 65536, "message": "最大长度为65536位"},
                                {"message": "最小长度为0位", "min": 0, "trigger": "blur"},
                                {"trigger": "blur"},
                            ],
                        },
                        {
                            "data": {"format": "string", "value": "新增属性中文测试"},
                            "index": 2006,
                            "name": "数据模板测试",
                            "rules": {"max": 10000, "min": 0, "required": False},
                            "type": "autotest",
                            "webRule": [
                                {"max": 10000, "message": "最大长度为10000位"},
                                {"message": "最小长度为0位", "min": 0, "trigger": "blur"},
                                {"trigger": "blur"},
                            ],
                        },
                    ],
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.message", "success")
            .assert_equal("body.status", 1)
            .assert_equal("body.data", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseHandleupdateEnt().test_start()
