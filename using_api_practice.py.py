
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
   
   #하위페이지 시작
   <!DOCTYPE html>
<html>
<head>
  <title>하위 페이지 1</title>
</head>
<body>
  <h1>하위 페이지 1</h1>
  <p>.</p>
</body>
</html>
