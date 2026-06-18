########## delete.md ##########
 book
<Book: Nineteen Eighty-Four>


>>> book.delete()
# Output:
(0, {'bookshelf.Book': 0})


>>> Book.objects.all()
# Output:
<QuerySet []>


from bookshelf.models import Book

book = Book.objects.get(title = "Nineteen Eighty-Four")

book.delete()
