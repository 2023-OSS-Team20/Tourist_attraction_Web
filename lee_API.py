import json
import requests
from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import urlopen

Key = "nzhfKajoHJmAX1gKiu5WyxWx2fbAfCxBWwOThdrb323YQrUlrW%2B1CmlnI3zWzZvdWwSHpP6665%2F8JdWBK1Pe4g%3D%3D"

#struct keyword

#abstract link class
class Linkmaker:
  def __init__(self):
    pass
  def search(self, keyword):
    pass
   
  
#location linkmaker

#keyword linkmaker
class KeywordLink(Linkmaker):
  def __init__(self):
    self.url = "http://apis.data.go.kr/B551011/KorService1/searchKeyword1?"
    self.queryParams = "serviceKey=" + Key + '&' + urlencode({
      quote_plus('MobileApp'): 'AppTest',
      quote_plus('MobileOS'): 'ETC',
      quote_plus('pageNo') : '1',
      quote_plus('numOfRows') : '10',                               
      quote_plus('_type') : 'json',
      quote_plus('listYN') : 'Y', 
      quote_plus('arrange') : 'A' ,   #제목 순 정렬
    })
    self.word = None
    self.searchURL = None
    
    
    
  def search(self,keyword):
    self.word = urlencode({quote_plus('keyword') : {keyword}})
    print(self.word)
    self.searchURL = self.url + self.queryParams + '&' + self.word
  
link = KeywordLink()
link.search("강릉")
 
search_url = link.searchURL 

print(search_url)

reqData = requests.get(search_url)
print(reqData.text)

#r_dict=json.loads(reqData.text)

#rDict = json.load(search_url)
