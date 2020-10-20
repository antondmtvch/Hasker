from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question
from .forms import QuestionForm


class IndexView(ListView):
    model = Question
    template_name = 'app/index.html'
    context_object_name = 'questions'
    queryset = Question.objects.select_related('author')


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'


class CreateQuestionView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = 'app/create_question.html'
    login_url = '/admin/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
