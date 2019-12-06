import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import Post

# Create your views here.


def add_data(request):
    int_num = random.randrange(10)
    title = "post" + str(int_num)
    body = "body of post" + str(int_num)
    Post.objects.create(title=title, body=body)
    return HttpResponse("add data: %s success" % title)


def article(request):
    # a = 5/0
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    print(post_list)
    return render(request, 'blog/article.html', context=context)


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/detail.html', context={"post": post})


def edit_post(request):
    print("path:", request.path)
    print("method:", request.method)
    print("encoding:", request.encoding)
    print("COOKIES:", request.COOKIES)
    print("session:", request.session)
    print("get_host", request.get_host())

    kw = request.GET.get('wd')
    user = request.GET.getlist('user')
    passwd = request.GET.get('passwd')
    print(kw, user, passwd)

    return render(request, 'blog/edit_post.html')


def update_post(request):
    post_id = request.POST.get("post_id")
    new_title = request.POST.get("title")
    new_body = request.POST.get("body")
    print(post_id, new_title, new_body)
    post = Post.objects.get(id=post_id)
    post.title = new_title
    post.body = new_body
    post.save()
    return HttpResponse("Yes")


def json_data(request):
    import json
    data = json.dumps({"user": "even", "passwd": "1234"})
    return HttpResponse(data, content_type="application/json")


def new_url(request):
    return  redirect("/admin")