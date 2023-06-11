from urllib.parse import urlencode, quote_plus

Key = "nzhfKajoHJmAX1gKiu5WyxWx2fbAfCxBWwOThdrb323YQrUlrW%2B1CmlnI3zWzZvdWwSHpP6665%2F8JdWBK1Pe4g%3D%3D"

#abstract link class
class Link:
  def __init__(self):
    pass
  def search(self):
    pass
  def pageNo(self):
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

  def pageNo(self,num):
    self.pNo = urlencode({quote_plus('pageNo') : num})

  def search(self, big, mid, small):      #big, mid 분류코드 형식 ex) A01 A0101 A01010100
    self.word = urlencode({
      quote_plus('cat1') : big,
      quote_plus('cat2') : mid,
      quote_plus('cat3') : small
      })
    
class IdLink(Link):
  def __init__(self):
    self.url = "http://apis.data.go.kr/B551011/KorService1/detailCommon1?"
    self.queryParams = "serviceKey=" + Key + '&' + urlencode({
      quote_plus('MobileApp'): 'AppTest',
      quote_plus('MobileOS'): 'ETC',                              
      quote_plus('_type') : 'json',
      quote_plus('firstImageYN') : 'Y',
      quote_plus('addrinfoYN') : 'Y',
      quote_plus('mapinfoYN') : 'Y',
      quote_plus('overviewYN') : 'Y',
      quote_plus('defaultYN') : 'Y'
    })
    self.word = None
    
  def search(self,Id):
    self.word = urlencode({quote_plus('contentId') : Id,})


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
  def __init__(self, big, mid, small):
    self.classlink = ClassLink()
    self.big = big
    self.mid = mid
    self.small = small
  
  def Create(self):
    self.classlink.search(self.big, self.mid, self.small)
    return self.classlink.url + self.classlink.queryParams + '&' + self.classlink.pNo + '&' + self.classlink.word
    
  def pageChange(self, number):
    self.classlink.pageNo(number)
    return self.classlink.url + self.classlink.queryParams + '&' + self.classlink.pNo + '&' + self.classlink.word
  
class IdLMaker(Linkmaker):
  def __init__(self, Id):
    self.Idlink = IdLink()
    self.Id = Id
  def Create(self):
    self.Idlink.search(self.Id)
    return self.Idlink.url + self.Idlink.queryParams + '&' + self.Idlink.word

'''

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

dlink = IdLMaker()

ID = IdLMaker(126508)
url = ID.Create()
print(url)
'''