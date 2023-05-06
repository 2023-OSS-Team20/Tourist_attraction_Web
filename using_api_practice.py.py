import json
import urllib.request

serviceKey  = '3Nb0/4jy/aClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK+XG2zjBWs35+Y2p290TbSABSuFU43hTShYnqHMtPakdGA=='

URL = 'http://apis.data.go.kr/B551011

-------
import urllib.request
key = "Nb0%2F4jy%2FaClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK%2BXG2zjBWs35%2BY2p290TbSABSuFU43hTShYnqHMtPakdGA%3D%3D"
url = "http://apis.data.go.kr/B551011/KorService1/areaCode1?serviceKey=key&numOfRows=10&pageNo=1&MobileOS=AND&MobileApp=appName"

content = urllib.request.request.get(url).content
print(content)


-------
import requests
import pprint
import json

url = 'http://apis.data.go.kr/B551011/KorService1/searchKeyword1?serviceKey=3Nb0/4jy/aClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK+XG2zjBWs35+Y2p290TbSABSuFU43hTShYnqHMtPakdGA==&pageNo=1&numOfRows=10&type=json'

response = requests.get(url)

contents = response.text

pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))

json_ob = json.loads(contents)
print(type(json_ob))

body = json_ob['response']['body']['items']
print(body)

import pandas as pd

dataframe = pd.json_normalize(body)

print(dataframe)
