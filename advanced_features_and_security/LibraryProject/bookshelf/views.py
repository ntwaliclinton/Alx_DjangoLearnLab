from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Post
from django.shortcuts import render
from .models import Book
from .forms import BookForm

# advanced_features_and_security/views.py
# Views that enforce permissions
@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def post_edit_view(request, pk):
     # This view requires the can_edit permission to access
    # ...

    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        # edit post logic
        pass
    return render(request, 'post_edit.html', {'post': post})

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def post_create_view(request):
       # This view requires the can_create permission to access
    # ...
    if request.method == 'POST':
        # create post logic
        pass
    return render(request, 'post_create.html')
"book_list", "books"


def book_list_view(request):
    books = Book.objects.all()  # Use ORM to fetch books
    return render(request, 'book_list.html', {'books': books})

def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Validate and sanitize user input using Django forms
            book = form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'form_example.html', {'form': form})