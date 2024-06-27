from django.shortcuts import render
import os
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from .models import Contracts


class ContractsListView(ListView):
    """Список контрактов"""

    template_name: str = 'contracts/contracts-list.html'
    queryset = Contracts.objects.all()
    context_object_name: str = 'contracts'

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        """Удаление неиспользуемых файлов с контрактами"""

        context: dict = super(ContractsListView, self).get_context_data(**kwargs)
        dir_files: str = os.path.abspath(os.path.join('files'))
        files: list = [contract.file for contract in Contracts.objects.all()]
        list_files: list = []
        for i in os.listdir(dir_files):
            for file in os.listdir((os.path.join(dir_files, i))):
                list_files.append(f"files/{i}/{file}")
        for file in list_files:
            if file not in files:
                os.remove(os.path.abspath(os.path.join(file)))
        return context


class ContractsCreateView(CreateView):
    """Создание контракта"""

    model = Contracts
    fields: tuple = 'customer', 'name', 'product', 'file', 'start_date', 'end_date', 'cost'
    success_url = reverse_lazy('contracts:contracts')

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ContractDetailView(DetailView):
    """Просмотр детальной страницы контракта"""

    template_name: str = 'contracts/contracts-detail.html'
    queryset = Contracts.objects.all()
    context_object_name: str = 'contracts'


class ContractsUpdateView(UpdateView):
    """Редактирование контракта"""

    model = Contracts
    fields: tuple = 'customer', 'name', 'product', 'file', 'start_date', 'end_date', 'cost'
    template_name_suffix: str = '_update_form'

    def get_success_url(self) -> str:
        return reverse('contracts:contracts-detail',
                       kwargs={"pk": self.object.pk})


class ContractsDeleteView(DeleteView):
    """Удаление контракта"""

    model = Contracts
    success_url = reverse_lazy('contracts:contracts')
