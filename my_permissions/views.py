from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from my_permissions.models import Message
from my_permissions.serializers import MessageSerializer


# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
