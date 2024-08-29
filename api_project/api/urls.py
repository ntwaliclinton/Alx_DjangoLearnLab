from django.urls import path
from .views import BookList
serializers.ModelSerializer
from rest_framework import serializers

urlpatterns = [
    path('api/books/', BookList.as_view(), name='book_list'),
]
