from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):


    def user_creation (self, email, username, password=None):
        if len(email) <= 0:
            raise ValueError('All Users must register an email address')

        # Create a new model based on email && username
        user = self.model(
            email=email,
            username=username)
        # Encrypt password with set_password function
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, username, password):
        user = self.user_creation(
            email,
            username=username,
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):


    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=60, unique=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    # Field for Authentication
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def get_username(self):
        return self.username

    # Return as string
    def __str__(self):
        return self.email
