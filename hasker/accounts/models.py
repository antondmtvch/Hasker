import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.staticfiles.storage import staticfiles_storage


def user_directory_path(instance, filename):
    filename, extension = os.path.splitext(filename)
    filename = str(uuid.uuid4()) + extension
    return 'avatars/{1}'.format(instance.id, filename)


class User(AbstractUser):
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return f'@{self.username}'

    def get_avatar_url(self):
        return self.avatar.url if self.avatar else staticfiles_storage.url('img/avatar.png')
