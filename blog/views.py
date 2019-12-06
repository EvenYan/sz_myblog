import random

from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

# Create your views here.


def add_data(request):
    int_num = random.randrange(10)
    title = "post" + str(int_num)
    body = "body of post" + str(int_num)
    Post.objects.create(title=title, body=body)
    return HttpResponse("add data: %s success" % title)


def article(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    print(post_list)
    return render(request, 'blog/article.html', context=context)


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/detail.html', context={"post": post})


def edit_post(request):
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
