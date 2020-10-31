from django.urls import path

from .views import QuestionDetailView, IndexView, CreateQuestionView, like_post, SearchQuestionView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question'),
    path('question/new/', CreateQuestionView.as_view(), name='create_question'),
    path('like/', like_post, name='like-post'),
    path('search/', SearchQuestionView.as_view(), name='search_question'),
]
