
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
# 페이징
def CategoryView(request, category_name):
    page = request.GET.get("page")
    category_posts = models.Post.objects.filter(category=category_name)
    paginator = Paginator(category_posts, 10)
    posts = paginator.get_page(page)
    categories = models.Category.objects.all()
    return render(
        request,
        "posts/categories.html",
        {
            "category_name": category_name,
            "category_posts": category_posts,
            "categories": categories,
            "posts": posts,
        },
    )
from django.core.paginator import Paginator

def my_view(request):
    items = MyModel.objects.all()
    paginator = Paginator(items, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'my_template.html', {'page_obj': page_obj})
