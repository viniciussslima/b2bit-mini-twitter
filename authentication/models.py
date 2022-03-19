from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class User(AbstractBaseUser):
    email = models.EmailField("email", max_length=255, unique=True)
    username = models.CharField("username", max_length=255, unique=True)
    description = models.TextField("description", max_length=255, blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
