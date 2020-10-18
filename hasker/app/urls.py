from django.urls import path

from .views import QuestionView, IndexView, CreateQuestion

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question'),
    path('question/new/', CreateQuestion.as_view(), name='ask_question'),
]
