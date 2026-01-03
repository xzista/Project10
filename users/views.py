from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import User
from .permissions import IsSelfOrAdmin
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return []
        if self.action in ("list", "retrieve"):
            return [IsAuthenticated()]
        if self.action in ("update", "partial_update"):
            return [IsAuthenticated(), IsSelfOrAdmin()]
        if self.action == "destroy":
            return [IsAdminUser()]
        return super().get_permissions()