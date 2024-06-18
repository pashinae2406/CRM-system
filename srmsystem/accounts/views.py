from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Employee
from django.contrib.auth.models import User
from leads.models import Leads


class RegisterView(CreateView):
    """Cтраница регистрации пользователей"""

    form_class = UserCreationForm
    template_name = 'accounts/register_form.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


class SignInView(LoginView):
    """Вход пользователей, имеющих назначенную администратором роль"""

    template_name = 'accounts/login_form.html'
    success_url = reverse_lazy('accounts:main-page')


class SignUpView(LogoutView):
    """Выход с сайта"""
    next_page = reverse_lazy("accounts:register")


class MainPageView(View):
    """Главная страница сайта"""

    def get(self, request):
        return render(request, 'accounts/main-page.html')




