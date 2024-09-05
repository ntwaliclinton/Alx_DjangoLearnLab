from rest_framework import serializers
from .models import Author, Book
import datetime
# BookSerializer serializes the fields of the Book model.
# Includes validation to ensure the publication year is valid.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# AuthorSerializer serializes the Author and nests the related books using the BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    # Nesting BookSerializer within AuthorSerializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
