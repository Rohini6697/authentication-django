
from django.urls import path

from .import views

urlpatterns = [
    path('', views.register,name='signup'),
    path('login/', views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard')
]
