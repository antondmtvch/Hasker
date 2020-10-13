from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractUser):
    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_directory_path)


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)


