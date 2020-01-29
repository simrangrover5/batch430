from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Login,Signup
from .models import Adduser
from django.views import View
from django.core.mail import send_mail
from random import randint
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,"users/index.html")
    #return HttpResponse("<h1 style='color:red'>This isUsers app</h1>")

def login(request):
    if request.session.get('email'):
        return HttpResponse("""
                <a href='/users/logout/'>LOGOUT</a>""")
    else:
        form = Login()
        return render(request,"users/login.html",{'f':form})

def afterlogin(request):
    form = Login(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            obj = Adduser.objects.get(email=email)
        except:
            error = "No such user...."
            form = Login()
            return render(request,"users/login.html",{'f':form,'error':error})
        else:
            if password == obj.password:
                request.session['email'] = email
                return HttpResponse("""Email : {} and password {}
                <a href='/users/logout/'>LOGOUT</a>""".format(email,password))
            else:
                error = "Invalid password"
                form = Login()
                return render(request,"users/login.html",{'f':form,'error':error})
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
            try:
                obj = Adduser.objects.get(email=data['email'])
            except Exception:   
                new_obj = Adduser.objects.create(**data)
                new_obj.save()
                form = Login()
                return render(request,"users/login.html",{'f':form})
            else:
                error = "User already exists...."
                form = Signup()
                return render(request,"users/signup.html",{'f':form,'error':error})
        else:
            error = "Invalid form...."
            form = Signup()
            return render(request,"users/signup.html",{'f':form,'error':error})
        

def forgot(request):
    subject = "Otp for forgot password to some foolish students.."
    otp = randint(1000,9999)
    message = "Your otp is " + str(otp)
    from_email = "simrangrover5@gmail.com"
    to_email = "tewarishivoham@gmail.com"
    send_mail(subject,message,from_email,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
    return HttpResponse("Hurray.........")

def logout(request):
    del request.session['email']
    return redirect('/users/login/')