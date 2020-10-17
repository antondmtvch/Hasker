from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('question/<int:question_id>/', question_view, name='question'),
    path('question/new/', ask_question_view, name='ask_question'),
]
