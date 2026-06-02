from models import *

books
author = Author.objects.get(name = "Joshua")
books_by_author = Book.objects.filter(author = author)


for book in books_by_author:
    print(book.title)

library = Library.objects.get(name = "Mosque")
books_in_lib = library.all()
librarian = Librarian.objects.filter(library = library)