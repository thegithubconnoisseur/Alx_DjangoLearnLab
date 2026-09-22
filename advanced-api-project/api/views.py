from django.shortcuts import render
from rest_framework import generics, permissions, filters, viewsets
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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
    filter_backends = [filters.SearchFilter, rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    # Rather than creating a filters.py file
    # i set the filterset_fields to handle names that contain
    # and match in upper and lower case forms for filtering
    filterset_fields = {
        "title" : ["iexact", "icontains"],
        "author__name" : ["iexact", "icontains"],
        "publication_year" : ["exact", "gte", "lte"]
        }
    search_fields = ['title','author']
    ordering_fileds = ["title","author", "publication_year"]
    # i set the defualt order to sort by publication_year from
    # latest to oldest then by title
    ordering = ["-publication_year", "title"]
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, rest_framework.DjangoFilterBackend]
    filterset_fields = {
        "title" : ["iexact", "icontains"],
        "author__name" : ["iexact", "icontains"],
        "publication_year" : ["exact", "gte", "lte"]
    }
    search_fields = ['title', 'author']
    ordering_fields = ["title", "author"]
    ordering = ["-publication_year", "title"]
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly]

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
