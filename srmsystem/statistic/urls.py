from django.urls import path
from .views import StatisticView


app_name: str = 'statistic'
urlpatterns: list = [
    path('statistic/', StatisticView.as_view(), name='statistic'),
]
