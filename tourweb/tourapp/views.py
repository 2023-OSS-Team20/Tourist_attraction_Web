from django.shortcuts import render
from tourapp.urlmake import Linkmaker, KeywordLmaker, ClassLmaker, IdLMaker
import json
import requests

linkmaker=Linkmaker()
      
class linkUrl():    
                     
    def create(self):
        pass

class keywordUrl(linkUrl):
    def __init__(self):
        self.keyword = 0
    
    def create(self,keyword):
        global linkmaker
        linkmaker = KeywordLmaker(keyword) #pagechange를 위해 전역변수사용 
        return linkmaker.Create()
    
class classUrl(linkUrl):
    def __init__(self):
        self.word = 0
        
    def create(self,word):
        global linkmaker
        linkmaker = ClassLmaker(word[0], word[1], word[2])
        return linkmaker.Create()

class idUrl(linkUrl):
    def __init__(self):
        self.intId = 0
    
    def create(self,id):
        self.intId = int(id)
        self.linkmaker = IdLMaker(self.intId) #Idlmaker는 pageChange할 필요 없음
        return self.linkmaker.Create()
    
class pageUrl(linkUrl):
    def __init__(self):
        self.num = 0
    
    def create(self, number):
        global linkmaker
        self.i = int(number)
        return linkmaker.pageChange(self.i)

class linkStrategy(object):     #여러 함수에서 호출되면서 하나만 존재해야함 -> singleton
    def __new__(cls): 
        if not hasattr(cls,'instance'):
            cls.instance = super(linkStrategy, cls).__new__(cls)
        return cls.instance
    
    def setlink(self, linkfac:linkUrl):
        self.linkfac = linkfac
    
    def create(self,word):
        return self.linkfac.create(word)
    '''
    def pNoChange(self,number):
        return self.linkfac.pageChange(number)
    '''    

def Keyword_result(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword',None)
        
    strat = linkStrategy()   
            
    strat.setlink(keywordUrl())
    url = requests.get(strat.create(keyword))  
    
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
    }    
    return render(request, 'tourapp/result.html', context)

def Class_result(request):   
    if request.method == 'GET':
        big = request.GET.get('big',None)
        mid = request.GET.get('mid',None)
        small = request.GET.get('small',None)
        word  =(big,mid,small)
    
    strat = linkStrategy()   
            
    strat.setlink(classUrl())
    url = requests.get(strat.create(word)) 
     
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
    }
    return render(request, 'tourapp/result.html', context)

def pageChange(request):
    if request.method == 'GET':
        num = request.GET.get('pnum')
    else:   #오류 처리를 위해
        num = 1    
        
    strat = linkStrategy()   
            
    strat.setlink(pageUrl())
    url = requests.get(strat.create(num))   
    
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data,
    }
    return render(request, 'tourapp/result.html', context)
    

def Id_result(request):
    if request.method == 'GET':
        Id = request.GET.get('contentsId',None)
        
    strat = linkStrategy()   
            
    strat.setlink(idUrl())
    url = requests.get(strat.create(Id)) 
    
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
    }
    return render(request, 'tourapp/detail.html', context)


def index(request):
    return render(request, 'tourapp/index.html')

