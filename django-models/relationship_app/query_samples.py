from relationship_app.models import Author,Book, Librarian,Library
author_name="jack"
author= Author.objects.get(name=author_name) 
books=Book.objects.filter(author=author)
library_name= "one"
library=Library.objects.get(name=library_name)
books=library.books.all()

library=Library.objects.get(name=library_name)
librarian=Librarian.objects.get(library=library) 

