from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addblog/',views.addblog),
    path('addblog1/',views.addblog1),
    path('allblog/',views.allblog),
    path('api/',views.showapi.as_view()),
]