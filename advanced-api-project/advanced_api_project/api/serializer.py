from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import date

# Book Serializer with a custom validation function
# To ensure that publication year is not in the future
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = '__all__'
    
    # overwritten validation method
    def validate(self, attribute):
        year = attribute.get("publication_year")
        if year and year > date.today().year:
            raise serializers.ValidationError({"publication_year" : "Publication year cannot be in the future"})
        return attribute

# Author serializer with a nested book serializer
# that is derived from the Book serializer with key name
# book
class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many = True, required = False)
    class Meta:
        model = Author
        fields = ['id', 'name', 'book']