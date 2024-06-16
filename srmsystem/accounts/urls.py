from django.urls import path
from .views import (RegisterView,
                    MainPageView,)


app_name = 'accounts'
urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path("login/", MainPageView.as_view(), name='login'),
]
