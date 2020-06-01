from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from users_api import permissions
from users_api import serializers
from users_api import models

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = (permissions.UpdateUser,)
