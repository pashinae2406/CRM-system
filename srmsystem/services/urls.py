from django.urls import path
from .views import (ServiceCreateView,
                    ServicesListView,
                    ServiceDeleteView,
                    ServiceDetailView,
                    ServiceUpdateView,)


app_name = 'services'
urlpatterns = [
    path("products/", ServicesListView.as_view(), name="services"),
    path('products/new/', ServiceCreateView.as_view(), name="service-create"),
    path('products/<int:pk>/', ServiceDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/delete/', ServiceDeleteView.as_view(), name="product-delete"),
    path('products/<int:pk>/edit/', ServiceUpdateView.as_view(), name="product-update"),
]
