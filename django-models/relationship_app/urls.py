from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
# relationship_app/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django Models project!")
