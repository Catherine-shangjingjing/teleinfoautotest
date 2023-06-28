# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/entapply/store_final.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseStoreFinal(HttpRunner):

    config = (
        Config("暂存企业注册第三步提交信息")
        .variables(**{"serOrg": "暂存服务托管单位"})
        .base_url("${ENV(HOST)}")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("暂存企业注册第三步提交信息")
            .post("/api/v3/entApply/hostingAndIdentifyServeInfo/storage")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                    "X-HTTP-Method-Override": "put",
                }
            )
            .with_cookies(**{"SESSION": "$entSession"})
            .with_json(
                {
                    "applyStep": 3,
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
                            "deployAddr": "致真",
                            "deployAddrCity": "110100",
                            "deployAddrCounty": "110101",
                            "deployAddrProvince": "110000",
                            "deployMode": 1,
                            "ipPort": None,
                            "name": None,
                            "sysType": 1,
                        },
                        {
                            "deployAddr": "致真",
                            "deployAddrCity": "110100",
                            "deployAddrCounty": "110101",
                            "deployAddrProvince": "110000",
                            "deployMode": 1,
                            "ipPort": None,
                            "name": None,
                            "sysType": 2,
                        },
                        {
                            "deployAddr": "天津",
                            "deployAddrCity": "120100",
                            "deployAddrCounty": "120101",
                            "deployAddrProvince": "120000",
                            "deployMode": 1,
                            "ipPort": None,
                            "name": None,
                            "sysType": 3,
                        },
                        {
                            "deployAddr": "天津",
                            "deployAddrCity": "120100",
                            "deployAddrCounty": "120101",
                            "deployAddrProvince": "120000",
                            "deployMode": 1,
                            "ipPort": None,
                            "name": None,
                            "sysType": 4,
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
                    "servHostingOrg": "$serOrg",
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
    TestCaseStoreFinal().test_start()
