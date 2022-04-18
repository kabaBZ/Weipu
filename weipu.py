import requests
from lxml import etree

url = 'http://qikan.cqvip.com/Search/SearchList'
params = {
    'G5tA5iQ4' : '5_RzZuNRr5e291xgCSl0gDHHd4wzlliOpRTckPoYFLYYuSOkBvoo2i3ZkDRFEgjhgfsO0YsEnIOvk43UqiIb7Ag3148.CH_ifa4FVnlPwox4aLnpmMVJNQOu9GRg3gLEEoXwh.2hdMprGwOFjEfmZD1Qa9uuUhMtC5Leoji6YrnGyh3K0xLh5uk0nRrdwYWComRfJg.QgrZ6tjKKpEoeCNXYTr9LqHYo1bBII2AmcM2dme5BDkRp8VCDjW_ZEZWZi2frbd9uUAuzleDBd7XpO_vWGuRfn4Oz3EnsGWWK0Qr9.re5NZcXDYJwA4NtkhdtMA01TEPt9iEYqgfHB45Cx6.0GsQZYkQJ1NcB7WCgwuAKhEp3dSUosqDKMrvt_IhKl',
}
headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Content-Length': '984',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'GW1gelwM5YZuS=5G7YsPua.jdZHgrZTbqOoNKSLl_LEdXaAWt7lu02oLNezGnKihIytyR2lvP54czMOxme_UmDrTAcVp0n9lbtP1A; ae51635ca5836b4864=94ee5fb45ad7f8f15d2d00578ab61262; 30e82fa753=c9d1538376cacc113f615e4718350312; ASP.NET_SessionId=oyywfutltbzokogexsxdeicy; Hm_lvt_540085501ec41c08ad1c432c82ab13d7=1650276511; Hm_lvt_fee827c3dc795c5122daf5ee854c1683=1650276511; Hm_lvt_17262dc62ce874a510e9c97140f381d6=1650276511; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%7D; search_isEnable=1; LIBUSERSETARTICLEPAGESIZECOOKIE=100; Hm_lpvt_540085501ec41c08ad1c432c82ab13d7=1650276617; Hm_lpvt_fee827c3dc795c5122daf5ee854c1683=1650276617; Hm_lpvt_17262dc62ce874a510e9c97140f381d6=1650276617; GW1gelwM5YZuT=5320gvKxwixgqqqDqHcXUJAx58d3Wtb3XPqd_4tCz7UWD600CE0Mc6G52HlYvX6LOYyhojQUUvk231D4pCmxKoplzB2MrKuHWkOO6EI0pH_aJ.2z8RoqqRoOYUDc7FQgWVo.VEvcfNRXJYz7Hn8NJzRjVEBd7Pu.bnvy8O29A0h6coSL3U.cHQtknuAuqzObEk3.nUaxrVouBC3y40iSKaTVKo1vKwnGtIG8zoXw9qreee8gdEaNzMAtOfpsCfdhLn_y6g_5fzrMB6zVJi_zIft80iaO9aS1p7S6HtFyFUxtYJ4M_NXPL1dBE4RE2Q6cebq692qeN6Lmd4x2vvylwtP',
    'Host': 'qikan.cqvip.com',
    'Origin': 'http://qikan.cqvip.com',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://qikan.cqvip.com/Qikan/Search/Advance?from=index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'searchParamModel' : {
        "ObjectType":1,
        "SearchKeyList":[{
            "FieldIdentifier":"M",
            "SearchKey":"人工智能",
            "PreLogicalOperator":"",
            "IsExact":"0"
        }],
        "SearchExpression":"",
        "BeginYear":"",
        "EndYear":"",
        "JournalRange":"",
        "DomainRange":"",
        "PageSize":"0",
        "PageNum":"1",
        "Sort":"0",
        "ClusterFilter":"",
        "SType":"",
        "StrIds":"",
        "UpdateTimeType":"",
        "ClusterUseType":"Article",
        "IsNoteHistory":1,
        "AdvShowTitle":"题名或关键词=人工智能",
        "ObjectId":"",
        "ObjectSearchType":"0",
        "ChineseEnglishExtend":"0",
        "SynonymExtend":"0",
        "ShowTotalCount":"0",
        "AdvTabGuid":"022aff87-deb9-557e-5b99-99ad5dd2949c"
    }
}
data_str = {
    'searchParamModel' : '%7B%22ObjectType%22%3A1%2C%22SearchKeyList%22%3A%5B%7B%22FieldIdentifier%22%3A%22M%22%2C%22SearchKey%22%3A%22%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22%2C%22PreLogicalOperator%22%3A%22%22%2C%22IsExact%22%3A%220%22%7D%5D%2C%22SearchExpression%22%3A%22%22%2C%22BeginYear%22%3A%22%22%2C%22EndYear%22%3A%22%22%2C%22JournalRange%22%3A%22%22%2C%22DomainRange%22%3A%22%22%2C%22PageSize%22%3A%220%22%2C%22PageNum%22%3A%221%22%2C%22Sort%22%3A%220%22%2C%22ClusterFilter%22%3A%22%22%2C%22SType%22%3A%22%22%2C%22StrIds%22%3A%22%22%2C%22UpdateTimeType%22%3A%22%22%2C%22ClusterUseType%22%3A%22Article%22%2C%22IsNoteHistory%22%3A1%2C%22AdvShowTitle%22%3A%22%E9%A2%98%E5%90%8D%E6%88%96%E5%85%B3%E9%94%AE%E8%AF%8D%3D%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22%2C%22ObjectId%22%3A%22%22%2C%22ObjectSearchType%22%3A%220%22%2C%22ChineseEnglishExtend%22%3A%220%22%2C%22SynonymExtend%22%3A%220%22%2C%22ShowTotalCount%22%3A%220%22%2C%22AdvTabGuid%22%3A%22022aff87-deb9-557e-5b99-99ad5dd2949c%22%7D'
}

response = requests.post(url = url ,headers = headers,json = data_str)
print(response.text)
with open('test.html','w') as fp:
    fp.write(response.text)
