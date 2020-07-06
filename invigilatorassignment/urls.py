from django.contrib import admin
from django.urls import path
from . import views
import teachers.views
import assigner.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('teachers/', teachers.views.home, name='teachers_home'),
    path('assigner/', assigner.views.home, name='assigner_home')
]
