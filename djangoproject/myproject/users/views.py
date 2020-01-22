from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login
# Create your views here.
def index(request):
    return render(request,"users/index.html")
    #return HttpResponse("<h1 style='color:red'>This isUsers app</h1>")

def login(request):
    form = Login()
    return render(request,"users/login.html",{'f':form})