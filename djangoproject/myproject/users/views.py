from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from .models import Adduser
from django.views import View
# Create your views here.
def index(request):
    return render(request,"users/index.html")
    #return HttpResponse("<h1 style='color:red'>This isUsers app</h1>")

def login(request):
    form = Login()
    return render(request,"users/login.html",{'f':form})

def afterlogin(request):
    form = Login(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        return HttpResponse("Email : {} and password {}".format(email,password))
    else:
        error = "Invalid form..."
        return render(request,"users/login.html",{'error':error})

def signup(request):
    form = Signup()
    return render(request,"users/signup.html",{'f':form})

class Aftersign(View):
    def get(self,request):
        error = "Invalid method"
        form = Signup()
        return render(request,"users/signup.html",{'f':form,'error':error})
    
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            data = {
            'username' : form.cleaned_data['username'],
            'email' : form.cleaned_data['email'],
            'password' : form.cleaned_data['password'],
            'pic' : form.cleaned_data['pic']
            }
            new_obj = Adduser.objects.create(**data)
            new_obj.save()
            form = Login()
            return render(request,"users/login.html",{'f':form})
        else:
            error = "Invalid form...."
            form = Signup()
            return render(request,"users/signup.html",{'f':form,'error':error})
        
