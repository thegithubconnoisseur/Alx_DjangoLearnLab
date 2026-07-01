from django.urls import path , include
from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename = 'book_all')

urlpatterns = [
    # Maps to the book list view
    path('books/', BookList.as_view(), name = 'book-list'),
    # Router URL for BookViewSet
    path('', include(router.urls)), # This includes all routes registered with the router
    # Token endpoint
    path('api-token-auth/', obtain_auth_token, name = "api_token_auth")
]