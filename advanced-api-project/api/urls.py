from django.urls import path, include
from .views import ListView
from .views import DetailView
from .views import CreateView
from .views import UpdateView
from .views import DeleteView
from .views import Authorview
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('author', Authorview)


urlpatterns = [
    path("books/", ListView.as_view()),
    path("books/<int:pk>/", DetailView.as_view()),
    path('books/create/', CreateView.as_view()),
    path("books/<int:pk>/update/", UpdateView.as_view()),
    path("books/<int:pk>/delete/", DeleteView.as_view()),
    path("", include(router.urls))
]