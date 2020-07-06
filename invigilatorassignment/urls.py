from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('teachers/', include('teachers.urls')),
    path('assigner/', include('assigner.urls')),
]
