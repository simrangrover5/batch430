from django.shortcuts import render
from django.http import HttpResponse
from .forms import Blog
from .models import Blogadd
from users.models import Adduser
# Create your views here.

def index(request):
    return HttpResponse("<h1 style='color:red'>This is blog app</h1>")

def addblog(request):
    form = Blog()
    return render(request,"blog/blog.html",{'f':form})

def addblog1(request):
    form = Blog(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        blog = form.cleaned_data['blog']
        data = {
            'author':Adduser.objects.get(email=request.session['email']),
            'title' : title,
            'blog' : blog
        }
        new_blog = Blogadd.objects.create(**data)
        new_blog.save()
        return render(request,"users/login1.html")
    else:
        error = "Invalid form"
        form = Blog()
        return render(request,"blog/blog.html",{'f':form})

def allblog(request):
    data = Blogadd.objects.all()
    allblogs=[]
    for obj in data:
        d = {
            'title':obj.title,
            'post':obj.blog,
            'author' : obj.author
        }
        allblogs.append(d)
    return render(request,"blog/allblogs.html",{'data':allblogs})