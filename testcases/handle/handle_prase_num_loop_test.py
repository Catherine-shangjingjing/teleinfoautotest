# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/handle/handle_prase_num_loop.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.login.login_admin_test import TestCaseLoginAdmin as LoginAdmin

from testcases.statistics.indexstatistics_test import (
    TestCaseIndexstatistics as Indexstatistics,
)

from testcases.handle.handleCreate_test import TestCaseHandlecreate as Handlecreate

from testcases.handle.resolveHandle_test import TestCaseResolvehandle as Resolvehandle

from testcases.statistics.indexstatistics_check_resolvNum_test import (
    TestCaseIndexstatisticsCheckResolvnum as IndexstatisticsCheckResolvnum,
)


class TestCaseHandlePraseNumLoop(HttpRunner):
    @pytest.mark.parametrize("param", Parameters({"biaoshi": "${get_dict(1)}"}))
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("解析标识1w")
        .variables(
            **{
                "handle": "$handle",
                "version": "$version",
                "prefix": "$prefix",
                "account": "${ENV(adminaccount)}",
                "password": "${ENV(adminpassword)}",
            }
        )
        .export(
            *["applyNum", "delnum", "entNum", "identityNum", "prefixNum", "resolvnum"]
        )
    )

    teststeps = [
        Step(RunTestCase("登录-管理员").call(LoginAdmin).export(*["adminSession"])),
        Step(
            RunTestCase("企业申请中统计")
            .call(Indexstatistics)
            .export(
                *[
                    "applyNum",
                    "entNum",
                    "identityNum",
                    "resolvnum",
                    "delnum",
                    "prefixNum",
                ]
            )
        ),
        Step(RunTestCase("标识注册").call(Handlecreate)),
        Step(RunTestCase("解析").call(Resolvehandle)),
        Step(RunTestCase("标识解析统计").call(IndexstatisticsCheckResolvnum)),
    ]


if __name__ == "__main__":
    TestCaseHandlePraseNumLoop().test_start()
