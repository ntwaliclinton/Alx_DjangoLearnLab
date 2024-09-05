# Advanced API Project

## Views

### BookListView
- **Endpoint:** `/books/`
- **Method:** GET
- **Description:** Retrieves a list of all books.
- **Permissions:** Public access (AllowAny)

### BookDetailView
- **Endpoint:** `/books/<int:pk>/`
- **Method:** GET
- **Description:** Retrieves details of a single book by ID.
- **Permissions:** Public access (AllowAny)

### BookCreateView
- **Endpoint:** `/books/create/`
- **Method:** POST
- **Description:** Creates a new book.
- **Permissions:** Authenticated users only

### BookUpdateView
- **Endpoint:** `/books/<int:pk>/update/`
- **Method:** PUT/PATCH
- **Description:** Updates an existing book.
- **Permissions:** Authenticated users only

### BookDeleteView
- **Endpoint:** `/books/<int:pk>/delete/`
- **Method:** DELETE
- **Description:** Deletes a book.
- **Permissions:** Authenticated users only
