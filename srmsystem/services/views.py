from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Service
from .forms import ServiceForm


class ServicesListView(ListView):
    """Отображение списка рекламных услуг"""

    template_name: str = "services/services-list.html"
    queryset = Service.objects.all()
    context_object_name: str = "products"


class ServiceCreateView(CreateView):
    """Создание услуги"""

    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("services:services")

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ServiceDeleteView(DeleteView):
    """Удаление услуги"""

    model = Service
    success_url = reverse_lazy('services:services')


class ServiceDetailView(DetailView):
    """Детальная страница услуги"""

    template_name: str = "services/service_details.html"
    queryset = Service.objects.all()
    context_object_name: str = "product"


class ServiceUpdateView(UpdateView):
    """Редактирование услуги"""

    model = Service
    form_class = ServiceForm
    template_name_suffix: str = "_update_form"

    def get_success_url(self) -> str:
        return reverse("services:product-detail",
                       kwargs={"pk": self.object.pk})
