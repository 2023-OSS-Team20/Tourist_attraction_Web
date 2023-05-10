import json
import requests
from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import urlopen

Key = "nzhfKajoHJmAX1gKiu5WyxWx2fbAfCxBWwOThdrb323YQrUlrW%2B1CmlnI3zWzZvdWwSHpP6665%2F8JdWBK1Pe4g%3D%3D"


'''
#URL 생성
URL = "http://apis.data.go.kr/B551011/KorService1/"
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
                              quote_plus('serviceKey'): {Key},
                              quote_plus('_type') : 'json',
                              quote_plus('arrange') : 'A' ,   #제목 순 정렬
                              quote_plus('areaCode') : {Area},
                              quote_plus('sigunguCode') : {Town},
                              quote_plus('keyword' ): {keyWord}
                              })



search_url = URL + queryParams
'''

#struct keyword

#abstract link class
class Linkmaker:
  def __init__(self):
    pass
  def make(self, keyword):
    pass
  
#location linkmaker

#keyword linkmaker

class KeywordLink(Linkmaker):
  def __init__(self):
    self.url = "http://apis.data.go.kr/B551011/KorService1/"
  



reqData = requests.get(search_url)
print(reqData.text)

#r_dict=json.loads(reqData.text)

rDict = json.load(search_url)
