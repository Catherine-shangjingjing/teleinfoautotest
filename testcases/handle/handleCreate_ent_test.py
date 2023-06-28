# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/handle/handleCreate-ent.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseHandlecreateEnt(HttpRunner):

    config = Config("标识注册-企业").base_url("${ENV(HOST)}").verify(False)

    teststeps = [
        Step(
            RunRequest("标识注册-企业")
            .post("/api/snms/identityv2/data")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Length": "2259",
                    "Content-Type": "application/json",
                    "Origin": "http://139.198.115.70:8000",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$entSession"})
            .with_json(
                {
                    "handle": "$handle",
                    "prefix": "$prefix",
                    "templateVersion": "$version",
                    "value": [
                        {
                            "auth": "",
                            "data": {
                                "format": "string",
                                "value": "2125654564tryrt混合类型JLHLH",
                            },
                            "index": 2000,
                            "name": "终端类型",
                            "rule": [
                                {
                                    "message": "必填项，不能为空",
                                    "required": False,
                                    "trigger": "blur",
                                },
                                {"message": "最小长度为0", "min": 0, "trigger": "blur"},
                                {
                                    "max": 65536,
                                    "message": "最大长度为65536",
                                    "trigger": "blur",
                                },
                            ],
                            "type": "terminalType",
                        },
                        {
                            "auth": "",
                            "data": {"format": "string", "value": "测试主体"},
                            "index": 2001,
                            "name": "所属主体",
                            "rule": [
                                {
                                    "message": "必填项，不能为空",
                                    "required": False,
                                    "trigger": "blur",
                                },
                                {"message": "最小长度为0", "min": 0, "trigger": "blur"},
                                {
                                    "max": 65536,
                                    "message": "最大长度为65536",
                                    "trigger": "blur",
                                },
                            ],
                            "type": "subject",
                        },
                        {
                            "auth": "",
                            "data": {"format": "string", "value": "测试用途"},
                            "index": 2002,
                            "name": "用途",
                            "rule": [
                                {
                                    "message": "必填项，不能为空",
                                    "required": False,
                                    "trigger": "blur",
                                },
                                {"message": "最小长度为0", "min": 0, "trigger": "blur"},
                                {
                                    "max": 65536,
                                    "message": "最大长度为65536",
                                    "trigger": "blur",
                                },
                            ],
                            "type": "useFor",
                        },
                        {
                            "auth": "",
                            "data": {"format": "string", "value": "dfjsldjfslfjls字符测试"},
                            "index": 2003,
                            "name": "串号或IMEI",
                            "rule": [
                                {
                                    "message": "必填项，不能为空",
                                    "required": False,
                                    "trigger": "blur",
                                },
                                {"message": "最小长度为0", "min": 0, "trigger": "blur"},
                                {
                                    "max": 65536,
                                    "message": "最大长度为65536",
                                    "trigger": "blur",
                                },
                            ],
                            "type": "serOrImei",
                        },
                        {
                            "auth": "",
                            "data": {"format": "string", "value": "中文测试中文测试"},
                            "index": 2004,
                            "name": "进网许可证编号",
                            "rule": [
                                {
                                    "message": "必填项，不能为空",
                                    "required": False,
                                    "trigger": "blur",
                                },
                                {"message": "最小长度为0", "min": 0, "trigger": "blur"},
                                {
                                    "max": 65536,
                                    "message": "最大长度为65536",
                                    "trigger": "blur",
                                },
                            ],
                            "type": "licenseNo",
                        },
                        {
                            "auth": "",
                            "data": {"format": "string", "value": "2408080数字测试"},
                            "index": 2005,
                            "name": "进网许可标志序号",
                            "rule": [
                                {
                                    "message": "必填项，不能为空",
                                    "required": False,
                                    "trigger": "blur",
                                },
                                {"message": "最小长度为0", "min": 0, "trigger": "blur"},
                                {
                                    "max": 65536,
                                    "message": "最大长度为65536",
                                    "trigger": "blur",
                                },
                            ],
                            "type": "licenseSign",
                        },
                        {
                            "auth": "",
                            "data": {"format": "string", "value": "新增属性中文测试"},
                            "index": 2006,
                            "name": "数据模板测试",
                            "rule": [
                                {
                                    "message": "必填项，不能为空",
                                    "required": False,
                                    "trigger": "blur",
                                },
                                {"message": "最小长度为0", "min": 0, "trigger": "blur"},
                                {
                                    "max": 10000,
                                    "message": "最大长度为10000",
                                    "trigger": "blur",
                                },
                            ],
                            "type": "autotest",
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
    TestCaseHandlecreateEnt().test_start()
