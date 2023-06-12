from django.shortcuts import render
from tourapp.urlmake import Linkmaker, KeywordLmaker, ClassLmaker, IdLMaker
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
    
linkfac = linkStrategy()

def Keyword_result(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
    else:   #오류 처리를 위해
        keyword = None    
            
    linkfac.setlink(KeywordLmaker(keyword))
    url = requests.get(linkfac.create())  
    
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data,
    }
    return render(request, 'tourapp/result.html', context)

def Class_result(request):   
    if request.method == 'GET':
        big = request.GET.get('big',None)
        mid = request.GET.get('small',None)
        small = request.GET.get('small',None)
    else:   #오류 처리를 위해
        big, mid, small = None 
    
    linkfac.setlink(ClassLmaker(big, mid, small))
    url = requests.get(linkfac.create())
    
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
    }
    return render(request, 'tourapp/result.html', context)

def pageChange(request):
    if request.method == 'GET':
        page_num = request.GET.get('pnum')
    else:   #오류 처리를 위해
        page_num = 1    
        
    intpnum = int(page_num)
    url = requests.get(linkfac.pNoChange(intpnum))  
    
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data,
    }
    return render(request, 'tourapp/result.html', context)
    

def Id_result(request):
    if request.method == 'GET':
        Id = request.GET.get('contentsId')
    else:   #오류 처리를 위해
        Id = None  
    
    intid = 0
    intId = int(Id)
    link = IdLMaker(intId)
    url = requests.get(link.Create())
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
    }
    return render(request, 'tourapp/detail.html', context)


def index(request):
    return render(request, 'tourapp/index.html')

