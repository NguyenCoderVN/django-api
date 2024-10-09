from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import MenuItems
from .serializers import MenuItemsSerializer


class MenuItemsView(GenericViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

    permission_classes = [DjangoObjectPermissions]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
