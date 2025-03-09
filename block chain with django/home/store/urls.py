from django.urls import path
from .views import get_storage, set_storage

urlpatterns = [
    path("get/", get_storage, name="get_storage"),
    path("set/", set_storage, name="set_storage")
]