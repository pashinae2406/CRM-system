from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from .models import Contracts


class ContractsListView(ListView):
    """Список контрактов"""

    template_name = 'contracts/contracts-list.html'
    queryset = Contracts.objects.all()
    context_object_name = 'contracts'


class ContractsCreateView(CreateView):
    """Создание контракта"""

    model = Contracts
    fields = 'name', 'product', 'file', 'start_date', 'end_date', 'cost'
    success_url = reverse_lazy('contracts:contracts')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ContractDetailView(DetailView):
    """Просмотр детальной страницы контракта"""

    template_name = 'contracts/contracts-detail.html'
    queryset = Contracts.objects.all()
    context_object_name = 'contracts'


class ContractsUpdateView(UpdateView):
    """Редактирование контракта"""

    model = Contracts
    fields = 'name', 'product', 'file', 'start_date', 'end_date', 'cost'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('contracts:contracts-detail',
                       kwargs={"pk": self.object.pk})


class ContractsDeleteView(DeleteView):
    """Удаление контракта"""

    model = Contracts
    success_url = reverse_lazy('contracts:contracts')
