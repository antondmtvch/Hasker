from django.contrib import admin

from .models import Answer, Question, Tag, User

admin.site.register((Answer, Question, Tag, User))
