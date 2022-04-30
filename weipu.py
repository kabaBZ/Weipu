import json

import requests
from lxml import etree
import re
import urllib3
urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'

url = 'http://qikan.cqvip.com/Search/SearchList'
flask_url = 'http://127.0.0.1:9420/cbb?type=S&webId=1001&data=tyt'
cookie_str = 'GW1gelwM5YZuS=5G7YsPua.jdZHgrZTbqOoNKSLl_LEdXaAWt7lu02oLNezGnKihIytyR2lvP54czMOxme_UmDrTAcVp0n9lbtP1A; Hm_lvt_540085501ec41c08ad1c432c82ab13d7=1650276511; Hm_lvt_fee827c3dc795c5122daf5ee854c1683=1650276511; Hm_lvt_17262dc62ce874a510e9c97140f381d6=1650276511; ae51635ca5836b4864=9412c3c5350c84c17f2255979cf15e34; ASP.NET_SessionId=lgheueqze12i1n1mvq225zq2; 30e82fa753=0de0d9d4bdbfdbc6315c3c04da3755a4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%7D; a48f5ec7b5=075acf59953577e481a10d15d668f262; 15debd6d1a=075acf59953577e481a10d15d668f262; search_isEnable=1; Hm_lpvt_17262dc62ce874a510e9c97140f381d6=1650446433; Hm_lpvt_fee827c3dc795c5122daf5ee854c1683=1650446433; Hm_lpvt_540085501ec41c08ad1c432c82ab13d7=1650446433; GW1gelwM5YZuT='
flask_response = requests.get(flask_url).text
print(flask_response)
weipu_url = url + re.findall('":"http://qikan.cqvip.com:80/Search/SearchList(.*?)","',flask_response)[0]
cookie_data = cookie_str + re.findall('false},"(.*?)"]]',flask_response)[0]
print(weipu_url)
headers = {
    'Host' : 'qikan.cqvip.com',
    'Proxy-Connection' : 'keep-alive',
    'Content-Length' : '984',
    'Pragma' : 'no-cache',
    'Cache-Control' : 'no-cache',
    'Accept' : 'text/html, */*; q=0.01',
    'X-Requested-With' : 'XMLHttpRequest',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin' : 'http://qikan.cqvip.com',
    'Referer' : 'http://qikan.cqvip.com/Qikan/Search/Advance?from=index',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie' : 'GW1gelwM5YZuS=5G7YsPua.jdZHgrZTbqOoNKSLl_LEdXaAWt7lu02oLNezGnKihIytyR2lvP54czMOxme_UmDrTAcVp0n9lbtP1A; Hm_lvt_540085501ec41c08ad1c432c82ab13d7=1650276511; Hm_lvt_fee827c3dc795c5122daf5ee854c1683=1650276511; Hm_lvt_17262dc62ce874a510e9c97140f381d6=1650276511; ae51635ca5836b4864=9412c3c5350c84c17f2255979cf15e34; ASP.NET_SessionId=lgheueqze12i1n1mvq225zq2; 30e82fa753=0de0d9d4bdbfdbc6315c3c04da3755a4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%7D; a48f5ec7b5=075acf59953577e481a10d15d668f262; 15debd6d1a=075acf59953577e481a10d15d668f262; search_isEnable=1; Hm_lpvt_540085501ec41c08ad1c432c82ab13d7=1650449356; Hm_lpvt_fee827c3dc795c5122daf5ee854c1683=1650449356; Hm_lpvt_17262dc62ce874a510e9c97140f381d6=1650449356; GW1gelwM5YZuT=GW1gelwM5YZuS=5G7YsPua.jdZHgrZTbqOoNKSLl_LEdXaAWt7lu02oLNezGnKihIytyR2lvP54czMOxme_UmDrTAcVp0n9lbtP1A; Hm_lvt_540085501ec41c08ad1c432c82ab13d7=1650276511; Hm_lvt_fee827c3dc795c5122daf5ee854c1683=1650276511; Hm_lvt_17262dc62ce874a510e9c97140f381d6=1650276511; ae51635ca5836b4864=9412c3c5350c84c17f2255979cf15e34; ASP.NET_SessionId=lgheueqze12i1n1mvq225zq2; 30e82fa753=0de0d9d4bdbfdbc6315c3c04da3755a4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221803c25318b3e8-05d4293d0358ae-48667e53-2073600-1803c25318c8a7%22%7D; a48f5ec7b5=075acf59953577e481a10d15d668f262; 15debd6d1a=075acf59953577e481a10d15d668f262; search_isEnable=1; Hm_lpvt_17262dc62ce874a510e9c97140f381d6=1650446433; Hm_lpvt_fee827c3dc795c5122daf5ee854c1683=1650446433; Hm_lpvt_540085501ec41c08ad1c432c82ab13d7=1650446433; GW1gelwM5YZuT=',
}
headers['Cookie'] = headers['Cookie'] + re.findall('false},"(.*?)"]]',flask_response)[0]
print(headers['Cookie'])
# data_str = {
#     'searchParamModel':'%7B%22ObjectType%22%3A1%2C%22SearchKeyList%22%3A%5B%7B%22FieldIdentifier%22%3A%22M%22%2C%22SearchKey%22%3A%22%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22%2C%22PreLogicalOperator%22%3A%22%22%2C%22IsExact%22%3A%220%22%7D%5D%2C%22SearchExpression%22%3A%22%22%2C%22BeginYear%22%3A%22%22%2C%22EndYear%22%3A%22%22%2C%22JournalRange%22%3A%22%22%2C%22DomainRange%22%3A%22%22%2C%22PageSize%22%3A%220%22%2C%22PageNum%22%3A%221%22%2C%22Sort%22%3A%220%22%2C%22ClusterFilter%22%3A%22%22%2C%22SType%22%3A%22%22%2C%22StrIds%22%3A%22%22%2C%22UpdateTimeType%22%3A%22%22%2C%22ClusterUseType%22%3A%22Article%22%2C%22IsNoteHistory%22%3A1%2C%22AdvShowTitle%22%3A%22%E9%A2%98%E5%90%8D%E6%88%96%E5%85%B3%E9%94%AE%E8%AF%8D%3D%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%22%2C%22ObjectId%22%3A%22%22%2C%22ObjectSearchType%22%3A%220%22%2C%22ChineseEnglishExtend%22%3A%220%22%2C%22SynonymExtend%22%3A%220%22%2C%22ShowTotalCount%22%3A%220%22%2C%22AdvTabGuid%22%3A%224b5c2716-0683-5d6c-11c4-cd4618373203%22%7D'
# }
# data = {"ObjectType":"1","SearchKeyList":[{"FieldIdentifier":"M","SearchKey":"人工智能","PreLogicalOperator":"","IsExact":"0"}],"SearchExpression":"","BeginYear":"","EndYear":"","JournalRange":"","DomainRange":"","PageSize":"0","PageNum":"1","Sort":"0","ClusterFilter":"","SType":"","StrIds":"","UpdateTimeType":"","ClusterUseType":"Article","IsNoteHistory":1,"AdvShowTitle":"题名或关键词=人工智能","ObjectId":"","ObjectSearchType":"0","ChineseEnglishExtend":"0","SynonymExtend":"0","ShowTotalCount":"0","AdvTabGuid":"4b5c2716-0683-5d6c-11c4-cd4618373203"}
data = {
    'searchParamModel' : '{"ObjectType":1,"SearchKeyList":[{"FieldIdentifier":"M","SearchKey":"人工智能","PreLogicalOperator":"","AfterLogicalOperator":null,"LeftBracket":null,"RighgtBracket":null,"IsExact":"0","ClusterShowName":null}],"SearchExpression":"","BeginYear":"","EndYear":"","UpdateTimeType":"","JournalRange":"","DomainRange":"","ClusterFilter":"OCC=2054#武汉大学","ClusterLimit":0,"ClusterUseType":"Article","UrlParam":"","Sort":"0","SortField":null,"UserID":"0","PageNum":1,"PageSize":20,"SType":"","StrIds":"","IsRefOrBy":0,"ShowRules":"++题名或关键词=人工智能++","IsNoteHistory":0,"AdvShowTitle":"题名或关键词=人工智能","ObjectId":"","ObjectSearchType":0,"ChineseEnglishExtend":0,"SynonymExtend":0,"ShowTotalCount":74066,"AdvTabGuid":"451f2cfa-52d4-952b-1921-7dfcb3ba694d"}'
}

data_str = json.dumps(data)
response1 = requests.post(url = weipu_url ,headers = headers,data = data)#,params = params,data ={'json':json.dumps(data)}
# response2 = requests.post(url = weipu_url ,headers = headers,data = data)
print(response1.status_code)

print(response1.text)

# with open('test.html','w') as fp:
#     fp.write(response1.text)
