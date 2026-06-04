from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("library/<int:pk>/",BookDetailView.as_view(), name ="library-detail"),
    path("list/", views.book_list, name = "list-books")
]