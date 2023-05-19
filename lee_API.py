import json
from msilib.schema import Class
import requests
from urllib.parse import urlencode, quote_plus

Key = "nzhfKajoHJmAX1gKiu5WyxWx2fbAfCxBWwOThdrb323YQrUlrW%2B1CmlnI3zWzZvdWwSHpP6665%2F8JdWBK1Pe4g%3D%3D"

#abstract link class
class Linkmaker:
  def __init__(self):
    pass
  def search(self, keyword):
    pass
  def make():
    pass
   
#keyword linkmaker
class KeywordLink(Linkmaker):
  def __init__(self):
    self.pNo = 1
    self.url = "http://apis.data.go.kr/B551011/KorService1/searchKeyword1?"
    self.queryParams = ""
    self.word = None
    self.searchURL = None
    
  def pNoinc(self):
    self.pNo += 1  
    
  def search(self,keyword):
    self.word = urlencode({quote_plus('keyword') : keyword})
    
  def make(self):
    self.queryParams = "serviceKey=" + Key + '&' + urlencode({
      quote_plus('MobileApp'): 'AppTest',
      quote_plus('MobileOS'): 'ETC',
      quote_plus('pageNo') : self.pNo,
      quote_plus('numOfRows') : '12',                               
      quote_plus('_type') : 'json',
      quote_plus('listYN') : 'Y', 
      quote_plus('arrange') : 'A' ,   #가나다 순 정렬
    })
    self.searchURL = self.url + self.queryParams + '&' + self.word

#classification linkmaker
class ClassLink(Linkmaker):
  def __init__(self):
    self.pNo = 1
    self.url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1?"
    self.queryParams =""
    self.word = None
    self.searchURL = None

  def search(self, big, mid):      #big, mid 분류코드 형식 ex) A01 A0101 A01010100
    self.word = urlencode({
      quote_plus('cat1') : big,
      quote_plus('cat2') : mid,
    })
    
  def pNoinc(self):
    self.pNo += 1
        
  def make(self):
    self.queryParams = "serviceKey=" + Key + '&' + urlencode({
      quote_plus('MobileApp'): 'AppTest',
      quote_plus('MobileOS'): 'ETC',
      quote_plus('pageNo') : self.pNo,
      quote_plus('numOfRows') : '12',                               
      quote_plus('_type') : 'json',
      quote_plus('listYN') : 'Y', 
      quote_plus('arrange') : 'A' ,   #가나다 순 정렬
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
clink.search("A01","A0101")
clink.make()
search_url = clink.searchURL 

print(search_url)

clink.pNoinc()
clink.make()
search_url = clink.searchURL

print(search_url)

##reqData = requests.get(search_url)
##print(reqData.text)



