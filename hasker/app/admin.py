from django.contrib import admin

from .models import Answer, Question, Tag, User, Like


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_date', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('create_date',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'published_date', 'author', 'flag')
    list_display_links = ('id', 'text')
    search_fields = ('text',)
    list_filter = ('published_date', 'flag')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')
    list_display_links = ('id', 'username')
    list_filter = ('is_staff',)


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Like, LikeAdmin)
