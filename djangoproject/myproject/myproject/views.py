from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("<h1 style='color:blue'>Welcome to about path</h1>")