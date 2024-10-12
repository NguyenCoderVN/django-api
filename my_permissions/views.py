from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from my_permissions.models import Message
from my_permissions.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    permission_classes = [DjangoModelPermissions]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
