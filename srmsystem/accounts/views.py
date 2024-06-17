from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Employee
from django.contrib.auth.models import User
from .forms import SignInForm
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


class SignInView(CreateView):
    form_class = SignInForm
    template_name = 'accounts/login_form.html'
    success_url = reverse_lazy('accounts:login')

    def post(self, request, *args, **kwargs):
        print(self.object)
        # user = User.objects.get(username=self.request.user.username)
        response = request
        # username = user.username
        # password = user.password
        # authenticate(self.request, username=username, password=password)
        # login(request=self.request, user=user)
        return response


class MainPageView(View):

    def get(self, request):
        return render(request, 'accounts/main-page.html')




