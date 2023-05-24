from urllib.parse import urlencode, quote_plus

Key = "nzhfKajoHJmAX1gKiu5WyxWx2fbAfCxBWwOThdrb323YQrUlrW%2B1CmlnI3zWzZvdWwSHpP6665%2F8JdWBK1Pe4g%3D%3D"

#abstract link class
class Link:
  def __init__(self):
    pass
  def search(self):
    pass
  def pageNo(int):
    pass
   
#keyword linkmaker
class KeywordLink(Link):
  def __init__(self):
    self.url = "http://apis.data.go.kr/B551011/KorService1/searchKeyword1?"
    self.queryParams = "serviceKey=" + Key + '&' + urlencode({
      quote_plus('MobileApp'): 'AppTest',
      quote_plus('MobileOS'): 'ETC',
      quote_plus('numOfRows') : '12',                               
      quote_plus('_type') : 'json',
      quote_plus('listYN') : 'Y', 
      quote_plus('arrange') : 'A' 
      #가나다 순 정렬
    })
    self.pNo = urlencode({quote_plus('pageNo') : 1})
    self.word = None
    self.searchURL = None

  def pageNo(self,num):
    self.pNo = urlencode({quote_plus('pageNo') : num})
    self.searchURL = self.url + self.queryParams + '&' + self.pNo + '&' +self.word

    
  def search(self,keyword):
    self.word = urlencode({quote_plus('keyword') : keyword})
    self.searchURL = self.url + self.queryParams + '&' + self.pNo + '&' +self.word

#classification linkmaker
class ClassLink(Link):
  def __init__(self):
    self.url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1?"
    self.queryParams = "serviceKey=" + Key + '&' + urlencode({
      quote_plus('MobileApp'): 'AppTest',
      quote_plus('MobileOS'): 'ETC',
      quote_plus('numOfRows') : '12',                               
      quote_plus('_type') : 'json',
      quote_plus('listYN') : 'Y', 
      quote_plus('arrange') : 'A' 
      #가나다 순 정렬
    })
    self.pNo = urlencode({quote_plus('pageNo') : 1})
    self.word = None
    self.searchURL = None

  def pageNo(self,num):
    self.pNo = urlencode({quote_plus('pageNo') : num})
    self.searchURL = self.url + self.queryParams + '&' + self.pNo + '&' +self.word

  def search(self, big, mid):      #big, mid 분류코드 형식 ex) A01 A0101 A01010100
    self.word = urlencode({
      quote_plus('cat1') : big,
      quote_plus('cat2') : mid,
    })
    self.searchURL = self.url + self.queryParams + '&' + self.pNo + '&' +self.word

'''
#factory
class Lmaker():
  def make(self) -> Link:
    
    
class KeywordLmaker(Lmaker):

class ClassLmaker(Lmaker):
  
#linkmakefunction
def keyLinkmake():
  
def classLinkmake():
'''

#main

keylink = KeywordLink()
keylink.search("카페")
 
search_url = keylink.searchURL 

print(search_url)

keylink.pageNo(3)

search_url = keylink.searchURL 

print(search_url)

'''
clink = ClassLink()
clink.search("A01","A0101")
search_url = clink.searchURL 

print(search_url)

clink.pageNo(3)
search_url = clink.searchURL

print(search_url)
'''


