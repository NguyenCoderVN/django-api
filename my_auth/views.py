from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, OAuth2Authentication
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from my_auth.serializers import UserSerializer


# Create your views here.
@api_view()
@permission_classes((IsAuthenticated, TokenHasReadWriteScope, ))
@authentication_classes((OAuth2Authentication,))
def auth_message(request):
    return Response("auth_message message here")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
