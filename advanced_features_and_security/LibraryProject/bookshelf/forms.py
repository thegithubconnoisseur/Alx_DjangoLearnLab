from django import forms 
from .models import Book


class ExampleForm(forms.ModelFrom):

    class Meta:
        model = Book
        fields = ["title", "author"]