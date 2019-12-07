from django.conf.urls import url
from blog.views import add_data, article, detail, edit_post, update_post, json_data, new_url, index, page, simple_login, logout, login, register


urlpatterns = [
    url(r'add_data/', add_data),
    url(r'articles/', article),
    url(r'post/(\d+)/', detail),
    url(r'edit_post/', edit_post),
    url(r'update_post/', update_post, name="updatepost"),
    url(r'json_data/', json_data),
    url(r'new_url/', new_url),
    url(r'index2/', index, name="index"),
    url(r'page/(\d+)', page, name="page"),
    url(r'simple_login', simple_login, name="simple_login"),
    url(r'logout', logout, name="logout"),
    url(r'login', login, name="login"),
    url(r'register', register, name="register"),
]
