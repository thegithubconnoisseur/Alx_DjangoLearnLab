from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .role_checks import is_member
from .models import UserProfile

@user_passes_test(is_member)
def member_view(request):
    user = UserProfile.objects.all()
    return render(request, "relationship_app/member_view.html", {"user": user})