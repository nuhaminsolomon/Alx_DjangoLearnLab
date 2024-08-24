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



# Permissions and Groups Configuration

This README file outlines how permissions and groups are set up in the Django application.

**Permissions:**

- **can_view_post:** Allows users to view posts.
- **can_create_post:** Allows users to create new posts.
- **can_edit_post:** Allows users to edit existing posts.
- **can_delete_post:** Allows users to delete posts.

**Groups:**

- **Editors:** Have permissions to view, create, and edit posts.
- **Moderators:** Have permissions to view, create, edit, and delete posts.
- **Admins:** Have full permissions to view, create, edit, delete, and publish posts.

**Configuration:**

1. **Define Custom Permissions:** In your `models.py` file, define custom permissions for the `Post` model:

   ```python
   class Post(models.Model):
       # ... other fields ...

       class Meta:
           permissions = [
               ("can_view_post", "Can view post"),
               ("can_create_post", "Can create post"),
               ("can_edit_post", "Can edit post"),
               ("can_delete_post", "Can delete post"),
           ]
