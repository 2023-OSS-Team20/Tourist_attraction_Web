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

-------
import json

# JSON 데이터
json_data = '{"name": ",CHOI", "age": 24, "city": "Seongnam"}'

# JSON 데이터를 파이썬 객체로 변환
data = json.loads(json_data)

# 파이썬 객체에서 원하는 데이터 추출
name = data['name']
age = data['age']
city = data['city']
# 추출한 데이터 출력
print(name)
print(age)
print(city)

