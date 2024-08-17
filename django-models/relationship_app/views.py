# relationship_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
