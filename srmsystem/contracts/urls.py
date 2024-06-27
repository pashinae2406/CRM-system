from django.urls import path
from .views import (ContractsListView,
                    ContractsCreateView,
                    ContractDetailView,
                    ContractsUpdateView,
                    ContractsDeleteView,)

app_name: str = 'contracts'
urlpatterns: list = [
    path('contracts/', ContractsListView.as_view(), name='contracts'),
    path('contracts/new/', ContractsCreateView.as_view(), name='contracts-create'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contracts-detail'),
    path('contracts/<int:pk>/edit/', ContractsUpdateView.as_view(), name='contracts-update'),
    path('contracts/<int:pk>/delete/', ContractsDeleteView.as_view(), name='contracts-delete'),
]
