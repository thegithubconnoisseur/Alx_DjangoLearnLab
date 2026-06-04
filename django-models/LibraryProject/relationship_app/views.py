from django.shortcuts import render
from .models import Book, Library
from django.views import View
from django.views.generic import DetailView

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request,'relationship_app/list_books.html', context)

class BookDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"


##################################################################################
class BookDetailViews(View):

    def book_detail(self,request):
        library = Library.object.all()
        context = {"library": library}
        return render(request,"relationship_app/library_detail.html",context)
    
    def get(self, request):
        return self.book_detail()
 #################################################################################   

