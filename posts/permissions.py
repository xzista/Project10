from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    """
    Разрешает доступ, если является администратором или автором (владельцем)
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user
