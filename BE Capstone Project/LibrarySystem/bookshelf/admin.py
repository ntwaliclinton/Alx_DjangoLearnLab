from django.contrib import admin
from .models import LibraryUser
from .models import Transaction
from .models import Book



class admin_model (admin.ModelAdmin):
     list_display = ('email','date_of_membership')

class Book_admin(admin.ModelAdmin):
        list_display = ('title','author','isbn','published_date','number_of_copies_available')


admin.site.register(Book,Book_admin)
admin.site.register(LibraryUser,admin_model)
admin.site.register(Transaction)