from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrOwner(BasePermission):
    """
    Разрешает чтение всем
    Изменение только если пользователь является администратором или автором (владельцем)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff or obj.author == request.user
