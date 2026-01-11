######### retrieve.md ##########
>>> Book.objects.filter(title = "1984").values()

# Output:
<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>

