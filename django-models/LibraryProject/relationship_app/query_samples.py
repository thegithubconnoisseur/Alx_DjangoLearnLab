from models import *

author_name = "Joshua"
author = Author.objects.get(name = author_name)
books_by_author = Book.objects.filter(author = author)


for book in books_by_author:
    print(book.title)

library_name = "mosque"
library = Library.objects.get(name = library_name)
books_in_lib = library.books.all()
librarian = Librarian.objects.filter(library = library)