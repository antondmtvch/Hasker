from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return f'@{self.username}'


class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-create_date', )


class Answer(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flag = models.BooleanField(default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.text[:50]

    class Meta:
        ordering = ('-published_date', )
