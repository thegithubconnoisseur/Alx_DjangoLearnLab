from django.db import models
from django.utils.text import slugify

# Create your models here.
# Author model witha string dunder mehtod, a slug field for the url
# and an overwritten save method to create the slug field to be the 
# mdoel name
class Author(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique = True, blank = True, null = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# This is a bood model with a title field, publication year in integer
# an author with a many books to author relationship to the book model
# a slug field and also an overwritten save method to save the model title 
# to the slugs field using slugify from django.utils.text
class Book(models.Model):
    title = models.CharField()
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'books')
    slug = models.SlugField(unique = True, blank = True, null = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)