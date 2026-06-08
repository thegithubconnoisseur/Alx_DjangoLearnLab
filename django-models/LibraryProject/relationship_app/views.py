from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
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
