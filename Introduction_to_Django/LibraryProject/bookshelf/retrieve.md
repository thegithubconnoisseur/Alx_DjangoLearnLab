######### retrieve.md ##########

book = Book.objects.get(title = "1984")
>>> book
<Book: 1984>
>>> book.__dict__
{'_state': <django.db.models.base.ModelState object at 0x1038520d0>, 'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}
