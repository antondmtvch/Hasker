from django.views.generic import ListView, DetailView, CreateView

from .models import Question
from .forms import QuestionForm


class IndexView(ListView):
    model = Question
    template_name = 'app/index.html'
    context_object_name = 'questions'


class QuestionView(DetailView):
    model = Question
    context_object_name = 'question'


class CreateQuestion(CreateView):
    form_class = QuestionForm
    template_name = 'app/ask_question.html'

