from django.shortcuts import render
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='ahome'),
    path('manual/', views.manual, name='manual'),
    path('<int:list_id>', views.list_detail, name='list_detail'),
    path('assigned/', views.assigned, name='assigned'),
]
