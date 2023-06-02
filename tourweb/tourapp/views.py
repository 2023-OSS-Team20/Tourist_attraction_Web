from django.shortcuts import render
from urlmake import KeywordLmaker
import json
import requests


def result(request):
    keyword = "에버"
    link = KeywordLmaker(keyword)
    url = requests.get(link.Create())
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
        
    }
    
    return render(request, 'tourapp/result.html', context)


def index(request):
    return render(request, 'tourapp/index.html')

# def result(request):
#     return render(request, 'tourapp/result.html')
