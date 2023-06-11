"""tourweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from tourapp.views import Keyword_result, index, Class_result ,pageChange, Id_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('Keyword_result/', Keyword_result, name='result'),
    path('Class_result/<str:big>/<str:mid>/<str:small>/',Class_result, name='result'),
    path('Id_result/', Id_result, name="Id_result"),
    path('pageChange/', pageChange, name="pageChange"),
]   
