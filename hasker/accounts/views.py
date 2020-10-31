from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .models import User
from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register_user.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()
            messages.info(request, 'Thanks for registering. You are now logged in.')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect(reverse_lazy('index'))
        return render(request, self.template_name, {'form': form})


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login_user.html'


class UserLogoutView(LogoutView):
    next_page = 'accounts:login'
