from rest_framework import serializers
from users_api import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'email', 'username', 'password')

        # Passwd field only availble for creating object
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    # we need to call the user_creation fn defined in Users, to ensure set_password is called
    def create(self, validated_data):

        user = models.User.objects.user_creation(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
