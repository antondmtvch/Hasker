from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Question, User, Answer, Like
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
    paginate_by = 10
    template_name = 'app/index.html'
    context_object_name = 'questions'
    queryset = Question.objects.select_related('author')


class QuestionDetailView(ListView):
    paginate_by = 5
    form = AnswerForm
    template_name = 'app/question_detail.html'

    def get_queryset(self):
        return get_object_or_404(Question, pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        question = self.get_queryset()
        context = self.get_context_data(object_list=question.get_answers())
        context['form'] = self.form()
        context['question'] = question
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        question = self.get_queryset()
        form = self.form(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.flag = True
            answer.save()
        return redirect(reverse('question', kwargs={'pk': question.id}))


class CreateQuestionView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = 'app/create_question.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required(login_url=reverse_lazy('login'))
def like_post(request):
    user = request.user
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        answer_obj = Answer.objects.get(pk=answer_id)
        if answer_obj.liked.filter(pk=user.pk):
            answer_obj.liked.remove(user)
        else:
            answer_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, answer_id=answer_id)
        if not created:
            if like.value == 1:
                like.value = 0
            else:
                like.value = 1
        like.save()
    return redirect('question', pk=answer_obj.question.pk)


class SearchQuestionView(ListView):
    model = Question
    template_name = 'app/search_question.html'
    context_object_name = 'questions'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return self.model.objects.none()
        if query.startswith('tag:'):
            query = query.replace('tag:', '').strip()
            object_list = self.model.objects.prefetch_related('author').filter(tags__name__exact=query)
        else:
            object_list = self.model.objects.prefetch_related('author').filter(
                Q(title__icontains=query) | Q(text__icontains=query))
        return object_list
