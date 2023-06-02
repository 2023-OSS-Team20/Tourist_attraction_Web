from django.shortcuts import render
from tourapp.urlmake import KeywordLmaker, ClassLmaker, IdLMaker
import json
import requests



def Keyword_result(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
    link = KeywordLmaker(keyword)
    url = requests.get(link.Create())
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
        
    }
    return render(request, 'tourapp/result.html', context)

def class_result(request):
    big = "A01"
    mid = "A0101"
    small = None
    
    link = ClassLmaker(big, mid, small)
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
