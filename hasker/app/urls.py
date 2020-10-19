from django.urls import path

from .views import QuestionView, IndexView, CreateQuestionView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question'),
    path('question/new/', CreateQuestionView.as_view(), name='ask_question'),
]
