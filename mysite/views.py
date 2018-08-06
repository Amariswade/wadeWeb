from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_list = []
    for count,post in enumerate(posts,1):
        post_list.append("No.{}：<b>{}</b><hr>".format(count,post.title))
        post_list.append(post.body+"<br>")
    return HttpResponse(post_list)

