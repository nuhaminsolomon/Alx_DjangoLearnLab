Alx_DjangoLearnLab
Alx_DjangoLearnLab


# Retrieving all books
books = Book.objects.all()

# Filtering books by author
books_by_author = Book.objects.filter(author='John Doe')

# Ordering books by published date
books_ordered = Book.objects.order_by('published_date')

# Creating a new book
new_book = Book(title='New Book', author='Jane Smith', published_date='2023-01-01')
new_book.save()



python manage.py startapp book_store
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book_store.apps.BookStoreConfig',
]



# Permissions and Groups Configuration for Books

This README file outlines how permissions and groups are set up for the `Book` model in the Django application.

**Permissions:**

- **can_view_book:** Allows users to view books.
- **can_create_book:** Allows users to create new books.
- **can_edit_book:** Allows users to edit existing books.
- **can_delete_book:** Allows users to delete books.

**Groups:**

- **Editors:** Have permissions to view, create, and edit books.
- **Viewers:** Have permissions to view books.
- **Admins:** Have full permissions to view, create, edit, and delete books.

**Usage**
- Use `@permission_required('my_app.can_edit', raise_exception=True)` to protect views.
- Assign users to groups via Django admin or programmatically.
**Configuration:**

1. **Define Custom Permissions:** In your `models.py` file, define custom permissions for the `Book` model:

   ```python
   class Book(models.Model):
       # ... other fields ...

       class Meta:
           permissions = [
               ("can_view_book", "Can view book"),
               ("can_create_book", "Can create book"),
               ("can_edit_book", "Can edit book"),
               ("can_delete_book", "Can delete book"),
           ]
