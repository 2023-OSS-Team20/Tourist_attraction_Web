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

------
# json 데이터 가공 연습 
import json

# json 파일 읽어오기
with open('./test.json', 'r', encoding='UTF8') as json_file:
    sample_json = json.load(json_file)
    print(sample_json)

# 출력: {'이름': '홍길동', '나이': 25, '특기': ['농구', '도술'], '가족관계': {'아버지': '홍판서', '어머니': '춘섬'}, '결혼 여부': True}

# json 문자열 읽어오기
json_str = '''
{
    "이름": "홍길동", 
    "나이": 25, 
    "특기": ["농구", "도술"], 
    "가족관계": {
        "아버지": "홍판서", 
        "어머니": "춘섬"
        }, 
    "결혼 여부": true
}
'''
sample_json2 = json.loads(json_str)
print(sample_json2)
# 출력: {'이름': '홍길동', '나이': 25, '특기': ['농구', '도술'], '가족관계': {'아버지': '홍판서', '어머니': '춘섬'}, '결혼 여부': True}



