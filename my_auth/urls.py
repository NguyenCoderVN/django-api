
from django.urls import path
from rest_framework import routers

from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('auth', views.auth_message, name='auth_message'),
    path('auth/token', obtain_auth_token, name='obtain_auth_token'),
]

urlpatterns += router.urls
