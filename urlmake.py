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
   
#keywordlink
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
    
  def pageNo(self,num):
    self.pNo = urlencode({quote_plus('pageNo') : num})
    self.searchURL = self.url + self.queryParams + '&' + self.pNo + '&' +self.word

    
  def search(self,keyword):
    self.word = urlencode({quote_plus('keyword') : keyword})

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

#abstract factory
class Linkmaker():
  def __init__():
    pass
  def Create():
    pass
  def pageChange():
    pass
    
class KeywordLmaker(Linkmaker):
  def __init__ (self, keyword):
    self.keylink = KeywordLink()
    self.keyword = keyword
  
    
  def Create(self):
    self.keylink.search(self.keyword)
    return self.keylink.url + self.keylink.queryParams + '&' + self.keylink.pNo + '&' + self.keylink.word
  
  def pageChange(self, number):
    self.keylink.pageNo(number)
    return self.keylink.url + self.keylink.queryParams + '&' + self.keylink.pNo + '&' + self.keylink.word
  


class ClassLmaker(Linkmaker):
  def __init__(self, big, mid):
    self.classlink = ClassLink()
    self.big = big
    self.mid = mid
  
  def Create(self):
    self.classlink.search(self.big, self.mid)
    
  def pageChange(self, number):
    self.classlink.pageNo(number)
    return self.classlink.url + self.classlink.queryParams + '&' + self.classlink.pNo + '&' + self.classlink.word



klink = KeywordLmaker("에버")

clink = ClassLmaker("A01","A0101")

url = klink.Create()
print(url)
url = klink.pageChange(2)
print(url)

url = clink.Create()
print(url)
url = klink.pageChange(3)
print(url)


