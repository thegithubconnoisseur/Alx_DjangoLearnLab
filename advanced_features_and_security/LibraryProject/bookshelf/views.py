from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
@permission_required("bookshelf.can_view", raise_exception = True)
def book_list(request):
    book = Book.objects.all()
    return render(request, "relationship_app/list_books.html",{"books": book})


@permission_required("bookshelf.can_create", raise_exception = True)
def can_create(request):

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get('publication_year')

        book = Book.objects.create(title = title, author = author, publication_year = publication_year)
        return redirect("list")
    return render(request, "relationship_app/add_book.html")


@permission_required("bookshelf.can_edit", raise_exception = True)
def can_edit(request,pk):

    book = Book.objects.get(id = pk)

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")

        book.title = title
        book.author = author 
        book.publication_year = publication_year

        book.save()
        return redirect("list")
    return render(request,"relationshi_app/change_book.html", {"book": book})



@permission_required("bookshelf.can_delete", raise_exception = True)
def can_delete(request, pk):
    book = Book.objects.get(id = pk)

    if request.method == "POST":
        book.delete()
        return redirect("list")
    return render(request,"relationshi_app/delete_book.html",{"book":book})