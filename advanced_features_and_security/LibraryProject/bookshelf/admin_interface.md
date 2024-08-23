# Django Admin Interface Configuration for Book Model

## Step 1: Register the Book Model
- Modified `bookshelf/admin.py` to register the `Book` model with the Django admin.

## Step 2: Customize the Admin Interface
- Implemented custom admin configurations:
  - Display fields: title, author, publication_year
  - Search fields: title, author
  - List filters: publication_year

## Step 3: Access the Admin Interface
- Created a superuser and accessed the Django admin at `http://127.0.0.1:8000/admin/`.
- Managed book entries using the customized admin interface.
