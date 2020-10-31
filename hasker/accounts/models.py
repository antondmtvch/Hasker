from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return f'@{self.username}'
