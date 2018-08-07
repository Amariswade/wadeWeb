from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
import datetime
from .models import Post
# Create your views here.
def homepage(request):
    template = get_template('homepage.html')
    posts = Post.objects.all()
    now = datetime.datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
def showpost(request,slug):
    template = get_template("detail.html")
    try:
        post = Post.objects.get(slug=slug)
        if(post!=None):
            html = template.render(locals())
            return HttpResponse(html)
    except Exception:
        return redirect("/")

