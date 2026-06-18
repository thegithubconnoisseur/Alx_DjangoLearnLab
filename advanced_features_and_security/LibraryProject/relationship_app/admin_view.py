from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .role_checks import is_admin

def is_admin(user):
    return (user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "ADMIN")

@user_passes_test(is_admin)
@permission_required("relationship_app.can_add_book", raise_exception = True)
@permission_required("relationship_app.can_change_book", raise_exception = True)
@permission_required("relationship_app.can_delete_book", raise_exception = True)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


