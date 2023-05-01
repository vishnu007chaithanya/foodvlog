from django.urls import path
from . import views



urlpatterns = [
    
    path('Register',views.register,name='Register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]