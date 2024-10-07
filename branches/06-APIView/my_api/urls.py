from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemList.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.MenuItem.as_view(), name='menu-items'),

]