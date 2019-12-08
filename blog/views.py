import random

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from blog.models import Post, UserInfo


# Create your views here.
from blog.utils import gen_secret


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
    return  redirect(reverse('page', args=(10, )))


def index(request):
    username = request.session.get('username')
    post_view = 90
    post_author = "Tom"
    post_body = "Hello, lllllllllllllllllllllll"
    evil_code = "<script>alert('你的电脑中毒了，请下载XXXX')</script>"
    context = {"num_list": [], "username": username, "post_view": post_view, "post_author": post_author, "post_body": post_body, "evil_code":evil_code}

    # 分页逻辑
    post_list = Post.my_objects.all()
    paginator = Paginator(post_list, 3)
    page_range = paginator.page_range
    page = paginator.page(1)
    page_post_list = page.object_list
    context.update({"page": page, "page_range": page_range, "page_post_list": page_post_list})
    return render(request, 'blog/home.html', context=context)


def page(request, num):
    post_list = Post.my_objects.all()
    paginator = Paginator(post_list, 3)
    page_range = paginator.page_range
    page = paginator.page(num)
    page_post_list = page.object_list
    context = {"page": page, "page_range": page_range, "page_post_list": page_post_list}
    return render(request, 'blog/home.html', context=context)


def simple_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        print(username, passwd)
        request.session['username'] = username
        resp = HttpResponse("登录成功")
        # resp.set_cookie("username", username, max_age=30)
        return resp
    return render(request, 'blog/simple_login.html')



def logout(request):
    resp = HttpResponse("会话删除成功")
    request.session.clear()
    return resp


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        passwd = gen_secret(passwd)
        print(username, passwd)
        user = UserInfo.objects.filter(username=username).filter(passwd=passwd).last()
        if user:
            request.session['username'] = username
            return HttpResponseRedirect(reverse('blog:index'))
        # request.session['username'] = username
        resp = HttpResponse("密码或者帐号输入错误， 请重新登录！")
        # resp.set_cookie("username", username, max_age=30)
        return resp
    return render(request, 'index.html')


def register(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    passwd = request.POST.get("passwd")
    passwd_confirm = request.POST.get("passwd_confirm")
    print(username, email, passwd, passwd_confirm)
    if passwd == passwd_confirm:
        passwd = gen_secret(passwd)
        UserInfo.objects.create(username=username, email=email, passwd=passwd)
        return HttpResponseRedirect(reverse("blog:login"))
    return HttpResponse("两次密码输入不一致，请重新输入！")