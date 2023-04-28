import requests
from bs4 import BeautifulSoup
import pandas as pd

API_key = "3Nb0%2F4jy%2FaClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK%2BXG2zjBWs35%2BY2p290TbSABSuFU43hTShYnqHMtPakdGA%3D%3D"

URL = "http://apis.data.go.kr/B551011/KorService1/searchKeyword1?numOfRows=12&MobileOS=ETC&MobileApp=AppTest&ServiceKey={API}&listYN=Y&arrange=A&areaCode=&sigunguCode=&cat1=&cat2=&cat3=&keyword=스파".format(API = API_key)
rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser")

practie =[]
for item in soup.find_all("item"):
    name = item.find("addr1").text
    practie.append(name)
print(name)