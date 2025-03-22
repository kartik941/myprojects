from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name = "home"),
    path("about",views.about,name = "about"),
    path("index",views.index,name = "home"),
    path("services",views.services,name = "services"),
    path("contact",views.contact,name = "contact"),
    path("login",views.login,name = "login"),
    path("register",views.register,name = "register"),
    path("forgot",views.forgot,name = "forgot"),
    
]
