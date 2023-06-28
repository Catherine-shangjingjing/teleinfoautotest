# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixAudit/register/submit_final_update.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseSubmitFinalUpdate(HttpRunner):

    config = (
        Config("testcase description")
        .variables(**{"prefix": "${get_prefix()}"})
        .base_url("${ENV(HOST)}")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("企业注册最终第三步提交信息")
            .post("/api/v3/entApply/update")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }
            )
            .with_cookies(**{"SESSION": "$entSession"})
            .with_json(
                {
                    "applyStep": 4,
                    "applyType": None,
                    "cltrid": None,
                    "contactCrtBackImgPath": None,
                    "contactCrtBackImgRid": "$imgId_b",
                    "contactCrtFrontImgPath": None,
                    "contactCrtFrontImgRid": "$imgId_f",
                    "contactCrtNo": "$contactCrtNo",
                    "contactCrtType": "$contactCrtType",
                    "contactEmail": "$contactEmail",
                    "contactName": "$contactName",
                    "contactPhone": "$contactPhone",
                    "createDate": "$createDate",
                    "dataHostingContractFilePath": None,
                    "dataHostingContractFileRid": None,
                    "dataHostingOrg": None,
                    "entGeneralId": None,
                    "entInfoLicenses": [],
                    "entInfoSerIndustrys": [],
                    "entInfoSyss": [
                        {
                            "deployAddr": "$entInfoSyss_0_deployAddr",
                            "deployAddrCity": "$entInfoSyss_0_deployAddrCity",
                            "deployAddrCounty": "$entInfoSyss_0_deployAddrCounty",
                            "deployAddrProvince": "$entInfoSyss_0_deployAddrProvince",
                            "deployMode": "$entInfoSyss_0_deployMode",
                            "ipPort": None,
                            "name": None,
                            "sysType": "$entInfoSyss_1_sysType",
                        },
                        {
                            "deployAddr": "$entInfoSyss_1_deployAddr",
                            "deployAddrCity": "$entInfoSyss_1_deployAddrCity",
                            "deployAddrCounty": "$entInfoSyss_1_deployAddrCounty",
                            "deployAddrProvince": "$entInfoSyss_1_deployAddrProvince",
                            "deployMode": "$entInfoSyss_1_deployMode",
                            "ipPort": None,
                            "name": None,
                            "sysType": "$entInfoSyss_2_sysType",
                        },
                        {
                            "deployAddr": "$entInfoSyss_2_deployAddr",
                            "deployAddrCity": "$entInfoSyss_2_deployAddrCity",
                            "deployAddrCounty": "$entInfoSyss_2_deployAddrCounty",
                            "deployAddrProvince": "$entInfoSyss_2_deployAddrProvince",
                            "deployMode": "$entInfoSyss_2_deployMode",
                            "ipPort": None,
                            "name": None,
                            "sysType": "$entInfoSyss_3_sysType",
                        },
                        {
                            "deployAddr": "$entInfoSyss_3_deployAddr",
                            "deployAddrCity": "$entInfoSyss_3_deployAddrCity",
                            "deployAddrCounty": "$entInfoSyss_3_deployAddrCounty",
                            "deployAddrProvince": "$entInfoSyss_3_deployAddrProvince",
                            "deployMode": "$entInfoSyss_3_deployMode",
                            "ipPort": None,
                            "name": None,
                            "sysType": "$entInfoSyss_3_sysType",
                        },
                    ],
                    "entPrefix": "$prefix",
                    "escrowId": None,
                    "escrowOrgName": None,
                    "establishDate": None,
                    "extDomain": None,
                    "extIpAddr": None,
                    "extWebName": None,
                    "finalAuditMsg": None,
                    "finalAuditStatus": None,
                    "firstAuditMsg": None,
                    "firstAuditStatus": None,
                    "id": "$applyId",
                    "idRegNaImp": None,
                    "industryCategory": "$industryCategory",
                    "industrySpecific": "$industrySpecific",
                    "isSubmit": 0,
                    "legalCrtBackImgContent": None,
                    "legalCrtBackImgPath": None,
                    "legalCrtBackImgRid": "$legalCrtBackImgRid",
                    "legalCrtFrontImgContent": None,
                    "legalCrtFrontImgPath": None,
                    "legalCrtFrontImgRid": "$legalCrtFrontImgRid",
                    "legalCrtNo": "$legalCrtNo",
                    "legalCrtType": "$legalCrtType",
                    "legalCrtTypeDesc": "$legalCrtTypeDesc",
                    "legalEmail": "$legalEmail",
                    "legalFax": None,
                    "legalName": "$legalName",
                    "legalPhone": "$legalPhone",
                    "orgAddr": "$orgAddr",
                    "orgAddrCity": "$orgAddrCity",
                    "orgAddrCityDesc": "$orgAddrCityDesc",
                    "orgAddrCounty": "$orgAddrCounty",
                    "orgAddrCountyDesc": "$orgAddrCountyDesc",
                    "orgAddrProvince": "$orgAddrProvince",
                    "orgAddrProvinceDesc": "$orgAddrProvinceDesc",
                    "orgCategorySpecificDesc": "$orgCategorySpecificDesc",
                    "orgCrtCode": "$orgCrtCode",
                    "orgCrtImgContent": None,
                    "orgCrtImgPath": None,
                    "orgCrtImgRid": "$orgCrtImgRid",
                    "orgCrtType": "$orgCrtType",
                    "orgDesc": None,
                    "orgName": "$orgName",
                    "orgNature": "$orgNature",
                    "orgNatureDesc": "$orgNature",
                    "periodValidity": None,
                    "regAuthority": None,
                    "regCapital": None,
                    "regRealNaImpName": None,
                    "regRealNaImpType": None,
                    "servHostingContractFilePath": None,
                    "servHostingContractFileRid": None,
                    "servHostingOrg": None,
                    "servSysBuildContractFilePath": None,
                    "servSysBuildContractFileRid": None,
                    "servSysBuildName": None,
                    "servSysBuildType": 1,
                    "servSysOperContractFilePath": None,
                    "servSysOperContractFileRid": None,
                    "servSysOperName": None,
                    "servSysOperType": 1,
                    "svtrid": None,
                    "thirdServiceMsg": None,
                    "thirdServiceStatus": None,
                    "updateDate": "$updateDate",
                    "userId": "$userId",
                    "userName": "$userName",
                    "website": None,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseSubmitFinalUpdate().test_start()
