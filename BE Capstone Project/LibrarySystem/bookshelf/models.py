# bookshelf/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

# Extend the User model to add library-specific fields
class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_membership = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    # Add related_name to prevent clashes with auth.User model
    groups = models.ManyToManyField(
        Group,
        related_name='libraryuser_groups',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='libraryuser_permissions',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    number_of_copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


# Transaction Model (Track check-outs and returns)
class Transaction(models.Model):
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.book.title} (Returned: {self.is_returned})'
