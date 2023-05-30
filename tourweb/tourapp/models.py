import urlmake
import json
import requests
from django.db import models

keyword = "에버"

klink = urlmake.KeywordLmaker(keyword)

url = requests.get(klink.Create())
text = url.text

data = json.loads(text)


print(data)
