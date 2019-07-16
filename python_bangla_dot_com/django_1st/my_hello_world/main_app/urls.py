from django.urls import path
from . import views     # dot(.) = current directory

urlpatterns = [
    path('', views.homeView, name="home"),
    path('home/', views.homeView, name="home"),
]
