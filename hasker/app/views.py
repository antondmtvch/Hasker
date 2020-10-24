from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question, User
from .forms import QuestionForm, AnswerForm, UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'app/register_user.html'


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'app/login_user.html'


class UserLogoutView(LogoutView):
    next_page = 'login'


class IndexView(ListView):
    model = Question
    paginate_by = 2
    template_name = 'app/index.html'
    context_object_name = 'questions'
    queryset = Question.objects.select_related('author')


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'


class CreateQuestionView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = 'app/create_question.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnswerQuestionView(CreateView):
    form_class = AnswerForm
