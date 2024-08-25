from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Post
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