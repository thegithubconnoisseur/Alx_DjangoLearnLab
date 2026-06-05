from django.shortcuts import render
from .models import Book
from .models import Library
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


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
