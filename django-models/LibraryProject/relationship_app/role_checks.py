def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "ADMIN"

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "LIBRARIAN"

def is_member(user):
    return user.is_authenticated and user.userprofile.role == "MEMBER"