from django.urls import path

from .views import QuestionDetailView, IndexView, CreateQuestionView, UserRegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question'),
    path('question/new/', CreateQuestionView.as_view(), name='create_question'),
]
