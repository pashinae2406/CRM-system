from django.urls import path
from .views import StatisticView


app_name = 'statistic'
urlpatterns = [
    path('statistic/', StatisticView.as_view(), name='statistic'),
]
