from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Leads
from .forms import LeadsForm


class LeadsListView(ListView):
    """Список потенцальных клиентов"""

    template_name = 'leads/leads-list.html'
    queryset = Leads.objects.all()
    context_object_name = 'leads'


class LeadsCreateView(CreateView):
    """Создание потенциального клиента"""

    model = Leads
    form_class = LeadsForm
    success_url = reverse_lazy('leads:leads')

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LeadsDetailView(DetailView):
    """Просмотр детальной страницы потенциального клиента"""

    template_name: str = "leads/leads-detail.html"
    queryset = Leads.objects.all()
    context_object_name: str = 'leads'


class LeadsUpdateView(UpdateView):
    """Редактирование потенциального клиента"""

    model = Leads
    form_class = LeadsForm
    template_name_suffix: str = '_update_form'

    def get_success_url(self) -> str:
        return reverse('leads:leads-detail',
                       kwargs={"pk": self.object.pk})


class LeadsDeleteView(DeleteView):
    """Удаление потенциального клиента"""

    model = Leads
    success_url = reverse_lazy('leads:leads')
