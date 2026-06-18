########## create.md ##########
>>>books = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

# Output:
>>> book
<Book: 1984>



######### retrieve.md ##########
>>> Book.objects.filter(title = "1984").values()

# Output:
<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>



########## update.md ##########
>>> Book.objects.filter(title = "1984").update(title = "Nineteen Eighty-Four")

# Output:
1


>>> book = Book.objects.get(title = "Nineteen Eighty-Four")
>>> book.save()
>>> book

# Output:
<Book: Nineteen Eighty-Four>


########## delete.md ##########
 book
<Book: Nineteen Eighty-Four>


>>> book.delete()
# Output:
(0, {'bookshelf.Book': 0})


>>> Book.objects.all()
# Output:
<QuerySet []>
