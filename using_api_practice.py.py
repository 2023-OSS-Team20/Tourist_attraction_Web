
 # 불러오기 ? 
 import requests

def get_api_data(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception('API request failed')
    
#2 
const fetchData = async () => {
    try {
      setError(null);
      setData(null);
      setLoading(true);

      const response = await axios.get(URL, {
        params: {
          serviceKey: process.env.REACT_APP_API_KEY,
          numOfRows: 1,
          pageNo: 10
        }
      });

      setData(response.data);
    } catch(e) {
      setError(e);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);
  
  if(loading) return <div>Loading...</div>;
  if(error)   return <div>Error...</div>;
  if(!data)   return null;
  
# python connect html
# json -> html 

def json_to_html(json_data):
    html = ""
    for key, value in json_data.items():
        html += "<p><strong>{0}:</strong> {1}</p>".format(key, value)
    return html
  
  html_data = json_to_html(json_data)

# url 매핑 
from django.urls import path
from myapp.views import display_html

urlpatterns = [
    path('', display_html, name='display_html'),
]
# render
from django.shortcuts import render

def index(request):
    return render(request, 'tourapp/index.html')

def result(request):
    return render(request, 'tourapp/result.html')

 
 
def show_json(request):
    with open('path/to/your/app/data.json') as f:
        json_data = json.load(f)
    return render(request, 'template.html', {'json_data': json_data})
from django.shortcuts import render
from django.http import HttpResponse
# call
def call_backend(request):
    result = backend_function()
    return render(request, 'frontend.html', {'result': result})
