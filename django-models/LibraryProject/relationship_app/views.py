from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .models import Library
from .models import Author
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .role_checks import is_admin


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request,'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        
    else:
        form = UserCreationForm()
    
    context = {"form": form}
    return render(request, "relationship_app/register.html", context)
        



# PERMISSION VIEWS
@permission_required('relationship_app.can_add_book', raise_exception = True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST["title"]
        author_name = request.POST["author"]

        author, created = Author.objects.get_or_create(name = author_name)
        Book.objects.create(title = title, author = author)
        return redirect('list-books')
    return render(request, 'relationship_app/add_book.html')


@permission_required("relationship_app.can_change_book", raise_exception = True)
def change_book(request, pk):
    book = get_object_or_404(Book,id = pk)

    if request.method == "POST":
    
        title = request.POST.get("title")
        book.title = title
        author_name = request.POST.get("author")
        author, created = Author.objects.get_or_create(name= author_name)
        book.author = author
        book.save()
        return redirect("list-books")
    return render(request,"relationship_app/change_book.html", {"book": book})


@permission_required("relationship_app.can_delete_book", raise_exception = True)
def delete_book(request,pk):
    book = Book.objects.get(id = pk)

    if request.method == "POST":
        book.delete()
        return redirect("list-books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
'''
##################################################################################
class BookDetailViews(View):

    def book_detail(self,request):
        library = Library.object.all()
        context = {"library": library}
        return render(request,"relationship_app/library_detail.html",context)
    
    def get(self, request):
        return self.book_detail()
 #################################################################################   
'''
