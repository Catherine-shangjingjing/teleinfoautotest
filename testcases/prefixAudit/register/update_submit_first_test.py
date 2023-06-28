# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/prefixAudit/register/update_submit_first.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseUpdateSubmitFirst(HttpRunner):

    config = (
        Config("企业注册第一步提交信息")
        .variables(
            **{
                "entprefix": "${ENV(prefix_second)}${get_random_param(1,10000000000,1)}",
                "companyCode": "${get_username()}",
                "orgName": "${get_username()}",
                "updateOrgName": "${get_username()}",
            }
        )
        .base_url("${ENV(HOST)}")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("企业注册第一步提交信息")
            .post("/api/v3/entApply/basicInfo/submit")
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
                    "applyStep": 2,
                    "applyType": None,
                    "area": ["110000", "110100", "110101"],
                    "cltrid": None,
                    "contactCrtBackImgPath": None,
                    "contactCrtBackImgRid": "$imgId_b",
                    "contactCrtFrontImgPath": None,
                    "contactCrtFrontImgRid": "$imgId_f",
                    "contactCrtNo": "$personId",
                    "contactCrtType": 1,
                    "contactEmail": "$email",
                    "contactName": "$entaccount",
                    "contactPhone": "$mobile",
                    "createDate": None,
                    "dataHostingContractFilePath": None,
                    "dataHostingContractFileRid": None,
                    "dataHostingOrg": None,
                    "entGeneralId": None,
                    "entInfoLicenses": [],
                    "entInfoSerIndustrys": [],
                    "entPrefix": "$entprefix",
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
                    "industry": ["A", "01"],
                    "industryCategory": "A",
                    "industrySpecific": "01",
                    "isSubmit": 0,
                    "legalCrtBackImgContent": None,
                    "legalCrtBackImgPath": None,
                    "legalCrtBackImgRid": "$imgId_b",
                    "legalCrtFrontImgContent": None,
                    "legalCrtFrontImgPath": None,
                    "legalCrtFrontImgRid": "$imgId_f",
                    "legalCrtNo": "$personId",
                    "legalCrtType": "1",
                    "legalCrtTypeDesc": "中国居民身份证",
                    "legalEmail": None,
                    "legalFax": None,
                    "legalName": "张三",
                    "legalPhone": None,
                    "orgAddr": "致真",
                    "orgAddrCity": "110100",
                    "orgAddrCityDesc": "市辖区",
                    "orgAddrCounty": "110101",
                    "orgAddrCountyDesc": "东城区",
                    "orgAddrProvince": "110000",
                    "orgAddrProvinceDesc": "北京市",
                    "orgCategorySpecificDesc": "农、林、牧、渔业-农业",
                    "orgCrtCode": "$companyCode",
                    "orgCrtImgContent": None,
                    "orgCrtImgPath": None,
                    "orgCrtImgRid": "$imgId",
                    "orgCrtType": "1",
                    "orgDesc": None,
                    "orgName": "$updateOrgName",
                    "orgNature": "1",
                    "orgNatureDesc": "国有控股",
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
                    "updateDate": None,
                    "userId": None,
                    "userName": None,
                    "website": None,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseUpdateSubmitFirst().test_start()
