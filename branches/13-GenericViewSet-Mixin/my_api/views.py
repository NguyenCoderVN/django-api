from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import MenuItems
from .serializers import MenuItemsSerializer


class MenuItemsView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
