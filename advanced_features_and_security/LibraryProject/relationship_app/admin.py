from django.contrib import admin
from .models import UserProfile, Book, Librarian
from .models import Author, Library

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "role")

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(Library)