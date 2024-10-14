# bookshelf/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Book, LibraryUser, Transaction
from .serializers import BookSerializer, LibraryUserSerializer, TransactionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['number_of_copies_available']
    search_fields = ['title', 'author', 'isbn']


class LibraryUserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # Action for checking out a book
    @action(detail=False, methods=['post'])
    def checkout(self, request):
        user_id = request.data.get('user')
        book_id = request.data.get('book')

        try:
            book = Book.objects.get(id=book_id)
            user = LibraryUser.objects.get(id=user_id)

            if book.number_of_copies_available <= 0:
                return Response({'error': 'No available copies'}, status=status.HTTP_400_BAD_REQUEST)

            # Create Transaction
            transaction = Transaction.objects.create(user=user, book=book)
            book.number_of_copies_available -= 1
            book.save()

            return Response({'message': 'Book checked out successfully'}, status=status.HTTP_201_CREATED)

        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        except LibraryUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Action for returning a book
    @action(detail=False, methods=['post'])
    def return_book(self, request):
        user_id = request.data.get('user')
        book_id = request.data.get('book')

        try:
            book = Book.objects.get(id=book_id)
            transaction = Transaction.objects.get(user__id=user_id, book__id=book_id, is_returned=False)

            transaction.return_date = timezone.now()
            transaction.is_returned = True
            transaction.save()

            book.number_of_copies_available += 1
            book.save()

            return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)

        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        except Transaction.DoesNotExist:
            return Response({'error': 'No active transaction for this user and book'}, status=status.HTTP_404_NOT_FOUND)
