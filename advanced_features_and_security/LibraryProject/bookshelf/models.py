from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager
from django.db import models
class CustomUserManager(BaseUserManager):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

   
class CustomUserManager(UserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(username, email, password, **extra_fields)
    # advanced_features_and_security/models.py


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

 # advanced_features_and_security/models.py
# Custom permissions for Post model
class Post(models.Model):
    # ...

    class Meta:
        permissions = (
            ('can_view', 'Can view post'),
            ('can_create', 'Can create post'),
            ('can_edit', 'Can edit post'),
            ('can_delete', 'Can delete post'),
        )
        # These permissions are used to control access to Post instances