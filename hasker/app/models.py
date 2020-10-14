from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractUser):
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_directory_path)


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class Answer(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flag = models.BooleanField(default=None)

