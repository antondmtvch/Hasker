from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import UserRegisterForm, UserLoginForm
from .models import User


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'accounts/register_user.html'


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login_user.html'


class UserLogoutView(LogoutView):
    next_page = 'accounts:login'
