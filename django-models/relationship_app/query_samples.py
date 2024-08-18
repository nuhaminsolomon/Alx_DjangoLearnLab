from relationship_app.models import Author,Book, Librarian,Library
author= Author.objects.get(id=1) 
books=Book.objects.filter(author=author)
library_name= "one"
library=Library.objects.get(name=library_name)
books=library.books.all()

library=Library.objects.get(name=library_name)
librarian=Librarian.objects.get(library=library) 

