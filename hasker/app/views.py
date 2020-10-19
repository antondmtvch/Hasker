from django.views.generic import ListView, DetailView, CreateView

from .models import Question
from .forms import QuestionForm


class IndexView(ListView):
    model = Question
    template_name = 'app/index.html'
    context_object_name = 'questions'


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'


class CreateQuestionView(CreateView):
    form_class = QuestionForm
    template_name = 'app/ask_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
