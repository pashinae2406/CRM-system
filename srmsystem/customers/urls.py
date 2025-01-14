from django.urls import path
from .views import (CustomersListView,
                    CustomersCreateView,
                    CustomersTransferView,
                    CustomersDeleteView,
                    CustomersDetailView,
                    CustomersUpdateView,)


app_name: str = 'customers'
urlpatterns: list = [
    path('customers/', CustomersListView.as_view(), name='customers'),
    path('customers/new/', CustomersCreateView.as_view(), name='customers-create'),
    path('customers/new/<int:pk>', CustomersTransferView.as_view(), name='customers-transfer'),
    path('customers/<int:pk>/delete/', CustomersDeleteView.as_view(), name='customers-delete'),
    path('customers/<int:pk>/', CustomersDetailView.as_view(), name='customers-detail'),
    path('customers/<int:pk>/edit/', CustomersUpdateView.as_view(), name='customers-update'),
]
