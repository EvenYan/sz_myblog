"""sz_myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import add_data, article, detail, edit_post, update_post, json_data, new_url, index, page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_data/', add_data),
    url(r'^articles/', article),
    url(r'^post/(\d+)/', detail),
    url(r'^edit_post/', edit_post),
    url(r'^update_post/', update_post),
    url(r'^json_data/', json_data),
    url(r'^new_url/', new_url),
    url(r'^index2/', index, name="index"),
    url(r'^page/(\d+)', page, name="page"),
]
