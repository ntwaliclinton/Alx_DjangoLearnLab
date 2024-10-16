# bookshelf/urls.py

from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LibraryUserViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', LibraryUserViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls
