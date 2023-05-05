import json
import requests
from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import urlopen

Key = "71wIrgVtoA73X2mMZ5VzxKcPT7cUGUdUle%2Be0w%2BwmCc5AO%2F6Oion4qdMPIKWLRlfJFzymt8YCoDf%2FAtpMoSMwA%3D%3D"



#URL 생성
URL = "http://apis.data.go.kr/B551011/KorService1/searchKeyword1"
#지역 코드변수
Area = "서울"
Town = "강남구"
#검색키워드
keyWord = "카페"


queryParams = '?' + urlencode({
                              quote_plus('MobileOS'): 'WIN',
                              quote_plus('numOfRows') : '10',
                              quote_plus('pageNo') : '1',                               
                              quote_plus('MobileApp'): 'AppTest',
                              quote_plus('serviceKey'): Key,
                              quote_plus('_type') : 'json',
                              quote_plus('arrange') : 'A' ,   #제목 순 정렬
                              quote_plus('areaCode') : Area,
                              quote_plus('sigunguCode') : Town,
                              quote_plus('keyword' ): keyWord
                              })

search_url = URL + queryParams



reqData = requests.get(search_url)
print(reqData.text)

r_dict=json.loads(reqData.text)

rDict = json.load(search_url)
