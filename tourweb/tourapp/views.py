from django.shortcuts import render
from urlmake import KeywordLmaker, ClassLmaker, IdLMaker
import json
import requests



def Keyword_result(request):
    keyword = "에버"
    link = KeywordLmaker(keyword)
    url = requests.get(link.Create())
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
        
    }
    return render(request, 'tourapp/result.html', context)

<<<<<<< HEAD
=======
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

>>>>>>> 8ede7feae3742c56a4400b74bd75df875d50471f

def index(request):
    return render(request, 'tourapp/index.html')

# def result(request):
#     return render(request, 'tourapp/result.html')
