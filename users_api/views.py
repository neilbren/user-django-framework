from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users_api import permissions
from users_api import serializers
from users_api import models


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = (permissions.UpdateUser,)
    authentication_classes = [TokenAuthentication,]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)
