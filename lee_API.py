import json
import requests
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen

Key = "71wIrgVtoA73X2mMZ5VzxKcPT7cUGUdUle%2Be0w%2BwmCc5AO%2F6Oion4qdMPIKWLRlfJFzymt8YCoDf%2FAtpMoSMwA%3D%3D"

#URL 생성
url = "https://apis.data.go.kr/B551011/KorService1/areaCode1"
queryParms = '?' + urlencode({
                              quote_plus('areaCode') : None,
                              quote_plus('serviceKey') : Key,
                              quote_plus('numOfRows') : '17',
                              quote_plus('pageNo') : '1',
                              quote_plus('MobileOS') : 'ETC',
                              quote_plus('MobileApp') : 'TestApp',
                              quote_plus('type') : 'json'
                            })
#최종 URL
Qurl = url + queryParms


reqData = requests.get(Qurl)
print(reqData.text)

r_dict=json.loads(reqData.text)

#rDict = json.load(Qurl)
