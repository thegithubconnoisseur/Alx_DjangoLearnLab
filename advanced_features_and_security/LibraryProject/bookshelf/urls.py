from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.book_list, name = "list"),
    path('create/', views.can_create, name = "create"),
    path("edit/<int:pk>/", views.can_edit, name = "edit"),
    path("delete/<int:pk>/", views.can_delete, name = "delete")
]