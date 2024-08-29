from django.urls import path
from .views import BookListCreateAPIView
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
urlpatterns = [
 path('api/books/', BookList.as_view(), name='book_list'),
 path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'books', BookViewSet)


