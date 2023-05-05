import json
import urllib.request

serviceKey  = '3Nb0/4jy/aClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK+XG2zjBWs35+Y2p290TbSABSuFU43hTShYnqHMtPakdGA=='

URL = 'http://apis.data.go.kr/B551011

-------
import urllib.request
key = "Nb0%2F4jy%2FaClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK%2BXG2zjBWs35%2BY2p290TbSABSuFU43hTShYnqHMtPakdGA%3D%3D"
url = "http://apis.data.go.kr/B551011/KorService1/areaCode1?serviceKey=key&numOfRows=10&pageNo=1&MobileOS=AND&MobileApp=appName"

content = urllib.request.request.get(url).content
print(content)
