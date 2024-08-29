from django.urls import path
from .views import BookListCreateAPIView
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
 path('api/books/', BookList.as_view(), name='book_list'),
 path('', include(router.urls)),
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

router = DefaultRouter()
router.register(r'books', BookViewSet)




