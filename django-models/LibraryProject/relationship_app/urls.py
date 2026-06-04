from django.urls import path
from .views import list_books, LibraryDetailView
from . import views


urlpatterns = [
    path("library/<int:pk>/",LibraryDetailView.as_view(), name ="library-detail"),
    path("list/", views.list_books, name = "list-books")
]