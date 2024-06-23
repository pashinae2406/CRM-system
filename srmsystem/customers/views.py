from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, View
from .models import Customers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from leads.models import Leads
from .forms import CustomerCreateForm, CustomerTransferForm


class CustomersListView(ListView):
    """Список активных клиентов"""

    model = Customers
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        for customer in Customers.objects.all():
            try:
                lead = Leads.objects.get(id=customer.lead_id)
                customer.first_name = lead.first_name
                customer.last_name = lead.last_name
                customer.phone = lead.phone
                customer.email = lead.email
                customer.ads = lead.ads
                customer.save()
                lead.delete()
            except:
                continue
        return context


class CustomersCreateView(CreateView):
    """Создание активного клиента"""

    model = Customers
    form_class = CustomerCreateForm
    success_url = reverse_lazy('customers:customers')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CustomersTransferView(CreateView):
    model = Customers
    form_class = CustomerTransferForm
    template_name = 'customers/customers_transfer_form.html'
    success_url = reverse_lazy('customers:customers')

    def get(self, request, *args, **kwargs):
        queryset = lead = Leads.objects.get(id=kwargs['pk'])
        form = CustomerCreateForm()
        print(form.is_valid())
        print(form.instance)
        form.instance.created_by = self.request.user
        return super().get(request, queryset=queryset, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(self)
        return super().post(request, *args, **kwargs)


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



