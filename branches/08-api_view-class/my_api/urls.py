from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.menu_items, name='menu-items'),
    path('menu-items/<int:pk>', views.MenuItemsView.menu_item, name='menu-item'),
]