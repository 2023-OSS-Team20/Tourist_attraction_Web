from django.shortcuts import render
from urlmake import Linkmaker,KeywordLmaker, ClassLmaker, IdLMaker
import json
import requests

class linkStrategy:
    def __init__(self):
        self.linkfac = 0
    
    def setlink(self, linkfac:Linkmaker):
        self.linkfac = linkfac
    
    def create(self):
        return self.linkfac.Create()
    
    def pNoChange(self,number):
        return self.linkfac.pageChange(number)

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

def Id_result(request):
    Id = "12650"
    
    link = IdLMaker(Id)
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
