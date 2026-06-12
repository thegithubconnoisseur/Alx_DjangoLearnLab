from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .role_checks import is_librarian

@user_passes_test(is_librarian)
@permission_required("relationship_app.can_add_book", raise_exception = True)
@permission_required("relationship_app.can_change_book", raise_exception = True)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")