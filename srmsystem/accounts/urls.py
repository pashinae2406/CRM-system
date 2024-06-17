from django.urls import path
from .views import (RegisterView,
                    SignInView,
                    MainPageView,)


app_name = 'accounts'
urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path("sign/", SignInView.as_view(), name='sign-in'),
    path("login/", MainPageView.as_view(), name='login'),
]
