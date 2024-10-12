from django.urls import path, include
from rest_framework import routers

from my_permissions import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
