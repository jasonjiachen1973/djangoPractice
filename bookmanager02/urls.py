"""bookmanager02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path, include



urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # 在include 的第二个参数中添加一个 namespace
    # 这样的话 我们的name 就变为了 namespace:name

    # namespaced 习惯上使用 子应用的名字
    re_path(r'^', include(('book.urls', 'book'), namespace='book')),
]