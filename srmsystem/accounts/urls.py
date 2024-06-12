from django.urls import path
from .views import RegisterApiView


app_name = 'accounts'
urlpatterns = [
    path('login/', RegisterApiView.as_view(), name="register"),
]
