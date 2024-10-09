from rest_framework import viewsets
from .models import MenuItems
from .serializers import MenuItemsSerializer


class MenuItemsView(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
