import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

API_key = unquote("71wIrgVtoA73X2mMZ5VzxKcPT7cUGUdUle%2Be0w%2BwmCc5AO%2F6Oion4qdMPIKWLRlfJFzymt8YCoDf%2FAtpMoSMwA%3D%3D")
URL = "http://apis.data.go.kr/B551011/KorService1/searchKeyword1?"
queryParams = '?' + urlencode(
    {
        quote_plus('ServiceKey'): API_key,
        quote_plus('MobileOS'): 'WIN',
        quote_plus('MobileApp'): 'AppTest',
        quote_plus('arrange'): 'A',
        quote_plus('keyword'): '스파',

    }
)

response = requests.get(URL + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

rows = xmlobj.findAll('item')
print(rows)
<<<<<<< HEAD
=======
# numOfRows=12&pageNo=1&MobileOS=ETC&MobileApp=AppTest&ServiceKey={API}&listYN=Y&arrange=A&areaCode=&sigunguCode=&cat1=&cat2=&cat3=&keyword=스파&_type=json".format(API = API_key)
# response = urlopen(URL)
# json_api = response.read().decode("utf-8")
# print(json_api)
>>>>>>> 783fe9680395df7766266da3e66136ec8db00eba
