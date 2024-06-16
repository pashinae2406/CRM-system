from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from leads.models import Leads


class RegisterView(CreateView):
    """Главная страница сайта"""

    form_class = UserCreationForm
    template_name = 'accounts/login_form.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        Leads.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        print(username)
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


class MainPageView(View):

    def get(self, request):
        return render(request, 'accounts/main-page.html')

