from django.db import models
from django.utils.text import slugify

# Create your models here.
# Author model with name and slug for the url
# with a custom save method to ensure that the 
# slug is named after the models name to be used in url
class Author(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# book model that has a many to one relationship 
# with the author model using the field name author
# This model also has an ovewritten save method to ensure
# that the slug name is created as the book title and 
# saved using the models.Model class
class Book(models.Model):
    title = models.CharField()
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'books')
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)