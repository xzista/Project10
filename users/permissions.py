from rest_framework.permissions import BasePermission

class IsSelfOrAdmin(BasePermission):
    """
    Разрешает доступ, если пользователь является администратором или работает со своим объектом User
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user