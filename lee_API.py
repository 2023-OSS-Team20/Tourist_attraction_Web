import json
from msilib.schema import Class
import requests
from urllib.parse import urlencode, quote_plus

Key = "nzhfKajoHJmAX1gKiu5WyxWx2fbAfCxBWwOThdrb323YQrUlrW%2B1CmlnI3zWzZvdWwSHpP6665%2F8JdWBK1Pe4g%3D%3D"
pNo = 1

#abstract link class
class Linkmaker:
  def __init__(self):
    pass
  def search(self, keyword):
    pass
   
#keyword linkmaker
class KeywordLink(Linkmaker):
  def __init__(self):
    self.url = "http://apis.data.go.kr/B551011/KorService1/searchKeyword1?"
    self.queryParams = "serviceKey=" + Key + '&' + urlencode({
      quote_plus('MobileApp'): 'AppTest',
      quote_plus('MobileOS'): 'ETC',
      quote_plus('pageNo') : pNo,
      quote_plus('numOfRows') : '12',                               
      quote_plus('_type') : 'json',
      quote_plus('listYN') : 'Y', 
      quote_plus('arrange') : 'A' ,   #가나다 순 정렬
    })
    self.word = None
    self.searchURL = None
    
    
    
  def search(self,keyword):
    self.word = urlencode({quote_plus('keyword') : keyword})
    self.searchURL = self.url + self.queryParams + '&' + self.word

#classification linkmaker
class ClassLink(Linkmaker):
    def __init__(self):
        self.url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1?"
        self.queryParams = "serviceKey=" + Key + '&' + urlencode({
        quote_plus('MobileApp'): 'AppTest',
        quote_plus('MobileOS'): 'ETC',
          quote_plus('pageNo') : pNo,
          quote_plus('numOfRows') : '12',                               
          quote_plus('_type') : 'json',
          quote_plus('listYN') : 'Y', 
          quote_plus('arrange') : 'A' ,   #가나다 순 정렬
        })
        self.word = None
        self.searchURL = None

    def search(self, big, mid, small):      #big, mid, small은 분류코드 형식 ex) A01 A0101 A01010100
        self.word = urlencode({quote_plus('cat1') : big,
                               quote_plus('cat2') : mid,
                               quote_plus('cat3') : small,
                               })
        self.searchURL = self.url + self.queryParams + '&' + self.word



#main
'''
keylink = KeywordLink()
keylink.search("카페")
 
search_url = keylink.searchURL 

print(search_url)

reqData = requests.get(search_url)
print(reqData.text)

'''
clink = ClassLink()
clink.search("A01","A0101","")

search_url = clink.searchURL 

print(search_url)

reqData = requests.get(search_url)
print(reqData.text)






r_dict=json.loads(reqData.text)
rDict = json.load(search_url)
