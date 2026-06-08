from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from .views import RegistrationView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view


urlpatterns = [
    path("library/<int:pk>/",LibraryDetailView.as_view(), name ="library-detail"),
    path("list/", views.list_books, name = "list-books"),
    path("registers/", RegistrationView.as_view(), name = "registers"),
    path("register/", views.register, name ='register'),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name = 'logout'),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html", next_page = "list-books"
                                     ), name = "login"),
    path("admin-view/", admin_view, name = "admin-view"),
    path("librarian-view/", librarian_view, name = 'librarian-view'),
    path("member-view/", member_view, name = 'member-view')
    

]