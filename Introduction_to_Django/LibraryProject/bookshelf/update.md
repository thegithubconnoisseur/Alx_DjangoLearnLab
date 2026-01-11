########## update.md ##########
>>> Book.objects.filter(title = "1984").update(title = "Nineteen Eighty-Four")

# Output:
1


>>> book = Book.objects.get(title = "Nineteen Eighty-Four")
>>> book.save()
>>> book

# Output:
<Book: Nineteen Eighty-Four>
