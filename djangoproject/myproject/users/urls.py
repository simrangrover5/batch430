from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('afterlogin/',views.afterlogin),
    path('signup/',views.signup),
    path('aftersign/',views.Aftersign.as_view())
]