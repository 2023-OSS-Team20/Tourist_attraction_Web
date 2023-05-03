import json
import urllib.request

serviceKey  = '3Nb0/4jy/aClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK+XG2zjBWs35+Y2p290TbSABSuFU43hTShYnqHMtPakdGA=='

URL = 'http://apis.data.go.kr/B551011


# 키워드 확인 
curl -X 'GET' \
  'https://apis.data.go.kr/B551011/KorService1/searchKeyword1?numOfRows=1&pageNo=1&MobileOS=WIN&MobileApp=Tour%20&keyword=%EA%B0%95%EC%9B%90&serviceKey=3Nb0%2F4jy%2FaClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK%2BXG2zjBWs35%2BY2p290TbSABSuFU43hTShYnqHMtPakdGA%3D%3D' \
  -H 'accept: application/json'
https://apis.data.go.kr/B551011/KorService1/searchKeyword1?numOfRows=1&pageNo=1&MobileOS=WIN&MobileApp=Tour%20&keyword=%EA%B0%95%EC%9B%90&serviceKey=3Nb0%2F4jy%2FaClfnlxLxtzqVHBrvqyF6AJ6DUemOzRK%2BXG2zjBWs35%2BY2p290TbSABSuFU43hTShYnqHMtPakdGA%3D%3D


<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <response>
    <header>
      <resultCode>0000</resultCode>
      <resultMsg>OK</resultMsg>
    </header>
    <body>
      <items>
        <item>
          <addr1>강원도 춘천시 서면 박사로 1210</addr1>
          <addr2>(서면) 부근</addr2>
          <areacode>32</areacode>
          <booktour>0</booktour>
          <cat1>A02</cat1>
          <cat2>A0205</cat2>
          <cat3>A02050200</cat3>
          <contentid>128778</contentid>
          <contenttypeid>12</contenttypeid>
          <createdtime>20060209090000</createdtime>
          <firstimage>http://tong.visitkorea.or.kr/cms/resource/71/181971_image2_1.jpg</firstimage>
          <firstimage2>http://tong.visitkorea.or.kr/cms/resource/71/181971_image3_1.jpg</firstimage2>
          <cpyrhtDivCd>Type3</cpyrhtDivCd>
          <mapx>127.7126856416</mapx>
          <mapy>37.9165380832</mapy>
          <mlevel>6</mlevel>
          <modifiedtime>20221228174959</modifiedtime>
          <sigungucode>13</sigungucode>
          <tel>
          </tel>
          <title>강원 경찰충혼탑</title>
        </item>
      </items>
      <numOfRows>1</numOfRows>
      <pageNo>1</pageNo>
      <totalCount>49</totalCount>
    </body>
  </response>
  
