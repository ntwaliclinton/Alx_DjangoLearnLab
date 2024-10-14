# LibrarySystem/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookshelf.urls')),  # or whatever app handles the API
]
