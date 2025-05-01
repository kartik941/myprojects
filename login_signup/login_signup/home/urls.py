from django.urls import path
from home.views import login_view, logout_view, dashboard, signup_view

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', signup_view, name='signup'),
    
]
