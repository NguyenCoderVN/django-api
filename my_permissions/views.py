from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, \
    DjangoObjectPermissions

from my_permissions.models import Message
from my_permissions.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    # permission_classes = [DjangoObjectPermissions]  # class changed

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):  # new function
        instance = serializer.save()
        assign_perm("delete_message", self.request.user, instance)
