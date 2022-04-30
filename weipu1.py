import requests
import re

flask_url = 'http://127.0.0.1:9420/cbb?type=S&webId=1001&data=tyt'
flask_response = requests.get(flask_url).text
print(flask_response)
weipu_url = re.findall('":"http://qikan.cqvip.com:80/Search/SearchList(.*?)","',flask_response)[0]
cookie_data = 'GW1gelwM5YZuT' + re.findall('false},"(.*?)"]]',flask_response)[0]
print(weipu_url)
print(cookie_data)