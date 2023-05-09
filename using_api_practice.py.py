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


-----
# 숙박정보 불러와 보기 
<response>
    <header>
      <resultCode>0000</resultCode>
      <resultMsg>OK</resultMsg>
    </header>
    <body>
      <items>
        <item>
          <addr1>경상북도 안동시 하회남촌길 69-5</addr1>
          <addr2>
          </addr2>
          <areacode>35</areacode>
          <benikia>
          </benikia>
          <cat1>B02</cat1>
          <cat2>B0201</cat2>
          <cat3>B02011600</cat3>
          <contentid>2465071</contentid>
          <contenttypeid>32</contenttypeid>
          <createdtime>20161220190700</createdtime>
          <firstimage>http://tong.visitkorea.or.kr/cms/resource/00/2626200_image2_1.jpg</firstimage>
          <firstimage2>http://tong.visitkorea.or.kr/cms/resource/00/2626200_image3_1.jpg</firstimage2>
          <cpyrhtDivCd>Type3</cpyrhtDivCd>
          <goodstay>
          </goodstay>
          <hanok>
          </hanok>
          <mapx>128.5175868107</mapx>
          <mapy>36.5376537450</mapy>
          <mlevel>6</mlevel>
          <modifiedtime>20230413082505</modifiedtime>
          <tel>054-855-8552</tel>
          <title>가경재 [한국관광 품질인증/Korea Quality]</title>
          <booktour>
          </booktour>
          <sigungucode>11</sigungucode>
        </item>
        <item>
