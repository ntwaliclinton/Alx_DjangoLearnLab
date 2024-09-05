from django.db import models

# Create your models here.
# Author model represents a writer with a one-to-many relationship to Book

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Book model represents a book with a title, year, and a foreign key to an Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
