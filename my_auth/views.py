from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from my_auth.serializers import UserSerializer


# Create your views here.
@api_view()
@permission_classes((IsAuthenticated, ))
def auth_message(request):
    if request.user.groups.filter(name="Manage").exists():
        return Response("Manage message here")
    else:
        return Response("You are not allowed to manage this message")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer