from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Customers
from leads.models import Leads


class CustomersListView(ListView):
    """Список активных клиентов"""

    template_name = 'customers/customers-list.html'
    queryset = Customers.objects.all()
    context_object_name = 'customers'


class CustomersCreateView(CreateView):
    """Создание активного клиента"""

    model = Customers
    fields = 'lead', 'contracts'
    success_url = reverse_lazy('customers:customers')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        # lead = Leads.objects.get(pk=self.object)
        print("lead: ", self.object, self.model.lead)
        return super().form_valid(form)


class CustomersDeleteView(DeleteView):
    """Удаление активного клиента"""

    model = Customers
    success_url = reverse_lazy("customers:customers")


class CustomersDetailView(DetailView):
    """Просмотр детальной страницы активного клиента"""

    template_name = 'customers/customers-detail.html'
    queryset = Customers.objects.all()
    context_object_name = 'customers'


class CustomersUpdateView(UpdateView):
    """Редактирование активного клиента"""

    model = Customers
    fields = 'lead', 'contracts'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('customers:customers-detail',
                       kwargs={"pk": self.object.pk})



