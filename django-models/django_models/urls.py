# django_models/urls.py

from django.contrib import admin
from django.urls import path, include
from relationship_app.views import home  # Make sure this import works

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This is the root URL
    path('relationship_app/', include('relationship_app.urls')),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]
