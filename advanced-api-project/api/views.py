from django.shortcuts import render
from rest_framework import generics, permissions, filters, viewsets
from .models import Book
from .models import Author
from .serializers import BookSerializer
from .serializers import AuthorSerializer

# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    # This allows the use of urlpath/?search =
    # to find or list data sets
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','author']
    permission_classes = [permissions.AllowAny]

    ## with modifying get  queryset isntead
    # when typing the url instead of using ?search to get query data
    # being looked for if you simply type  ?field = values
    # you get the data set being queried for 
    # to do this
    def get_queryset(self):
        queryset = Book.objects.all()

        author = self.request.query_params.get("author")
        if author:
            queryset = queryset.filter(author__icontains = author)
        return queryset

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Book.objects.all()

        author = self.request.query_params.get("author")
        if author:
            queryset = queryset.filter(author__iexact = author)
        return queryset

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','author']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()

        author = self.request.query_params.get("author")
        if author:
            queryset = queryset.filter(auhtor__iexact = author)
        return queryset

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fileds = ['title', 'author']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()

        author = self.request.query_params.get("author")
        if author:
            queryset = queryset.filter()
        return queryset
    
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()

        author = self.request.query_params.get("author")
        if author:
            queryset = queryset.filter(author__iexact = author)
        return queryset
    
class Authorview(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
