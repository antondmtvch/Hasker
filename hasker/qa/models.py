from django.conf import settings
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('-create_date', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.pk})

    def get_answers(self):
        return self.answer_set.select_related('author').order_by('-published_date')


class Answer(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='author')
    flag = models.BooleanField(default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.text[:50]

    @property
    def num_likes(self):
        return self.liked.all().count()

    class Meta:
        ordering = ('-published_date', )


class Like(models.Model):
    LIKE_CHOICES = (
        (1, 'Like'),
        (0, 'Dislike'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=LIKE_CHOICES, default=1)

    def __str__(self):
        return f'{self.answer.id} | {self.value}'
