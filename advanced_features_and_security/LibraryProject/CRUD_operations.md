# CRUD Operations

## Create Operation
Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
1984
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
Nineteen Eighty-Four
book.delete()
print(Book.objects.all())
<QuerySet []>
