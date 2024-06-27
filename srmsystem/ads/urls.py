from django.urls import path
from .views import (AdsListView,
                    AdsCreateView,
                    AdsDeleteView,
                    AdsDetailView,
                    AdsUpdateView,
                    AdsStatisticView,)


app_name: str = 'ads'
urlpatterns: list = [
    path('ads/', AdsListView.as_view(), name='ads'),
    path('ads/new/', AdsCreateView.as_view(), name='ads-create'),
    path('ads/<int:pk>/delete/', AdsDeleteView.as_view(), name='ads-delete'),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name='ads-detail'),
    path('ads/<int:pk>/edit/', AdsUpdateView.as_view(), name='ads-update'),
    path('ads/statistic/', AdsStatisticView.as_view(), name='ads-statistic'),
]
