from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<str:room>/',views.Room, name="room"),
    path('checkview', views.checkview, name='checkview'),
]