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
from .serializers import UserSerializer
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
#    permission_classes = (permissions.UpdateUser,)
    authentication_classes = [TokenAuthentication,]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
