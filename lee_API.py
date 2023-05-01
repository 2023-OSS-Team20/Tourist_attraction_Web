import json
import requests
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen

serviceKey = "71wIrgVtoA73X2mMZ5VzxKcPT7cUGUdUle%2Be0w%2BwmCc5AO%2F6Oion4qdMPIKWLRlfJFzymt8YCoDf%2FAtpMoSMwA%3D%3D"
url = "http://apis.data.go.kr/B551011/KorService1/areaCode1"
queryParms = '?' + urlencode({quote_plus('areaCode') : None,
                              quote_plus('servicekey') : serviceKey,
                              quote_plus('numOfRows') : '17',
                              quote_plus('pageNo') : '1',
                              quote_plus('MobileOs') : 'ETC',
                              quote_plus('MobileApp') : 'TestApp',
                              quote_plus('type') : 'json'})

response = urlopen(url + queryParms)