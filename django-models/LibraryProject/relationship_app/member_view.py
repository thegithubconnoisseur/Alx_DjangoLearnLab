from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .role_checks import is_member
from .models import UserProfile

@user_passes_test(is_member)
@permission_required("relationship_app.can_add_book", raise_exception = True)
def member_view(request):
    profile = UserProfile.objects.get(user = request.user)
    return render(request, "relationship_app/member_view.html", {"profile": profile})