from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):


    def user_creation (self, email, name, DOB, password=None):
        if len(email) <= 0:
            raise ValueError('All Users must registered an email address')

        # Create a new model based on email, name & DOB
        user = self.model(email=email, name=name, DOB=DOB)
        # Encrypt password with set_password function
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password, DOB):
        user = self.user_creation(
            email,
            name=name,
            password=password,
            DOB=DOB,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):


    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=30)
    DOB = models.DateField()
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()

    # Field for Authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    REQUIRED_FIELDS = ['DOB']


    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.DOB
    # Return as string
    def __str__(self):
        return self.email
