from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='thome'),
    path('<int:product_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
]