from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import date

# Created a book serializer class to list book models
# This comes with a custom made author related field that is written
# so that author comes with its string dunder method
class BookSerializer(serializers.ModelSerializer):
    # created an author name becuase author is a required field that accepts id
    # on postman and for some reason it keeps requiring the author field
    author_name = serializers.StringRelatedField(source = 'author', read_only = True )
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'author_name', 'slug']

    # Validate here is overwritten to raise a validation error on the serializer
    # if  year input in the model is greater than todays year
    def validate(self, attribute):
        year = attribute.get("publication_year")

        if year and year > date.today().year:
            raise serializers.ValidationError({"publication_year" : "Publication year cannot be in the future"})
        return attribute

# Author serializer class created with a books custome field 
# this book field is drawn from the book serializer and can be multiple but is not required 
# to make author serializer object
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

