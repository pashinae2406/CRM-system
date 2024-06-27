from django.urls import path
from .views import (RegisterView,
                    SignInView,
                    SignUpView,
                    MainPageView,)


app_name: str = 'accounts'
urlpatterns: list = [
    path("", RegisterView.as_view(), name="register"),
    path("login/", SignInView.as_view(), name='login'),
    path("logout/", SignUpView.as_view(), name='logout'),
    path("main/", MainPageView.as_view(), name='main-page'),
]
