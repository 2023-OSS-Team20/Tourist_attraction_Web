from django.shortcuts import render
import urlmake
import json
import requests

def result_view(request):
    keyword = "에버"
    link = urlmake.KeywordLmaker(keyword)
    url = requests.get(link.Create())
    text = url.text
    data = json.loads(text)
    
    context = {
        'data': data
    }
    
    return render(request, 'result.html', context)




def index(request):
    return render(request, 'tourapp/index.html')

def result(request):
    return render(request, 'tourapp/result.html')
