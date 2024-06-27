from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .models import Ads
from .commands import count_of_leads, count_of_customers, profit_ads
from contracts.models import Contracts


class AdsListView(ListView):
    """Список рекламных компаний"""

    template_name: str = 'ads/ads-list.html'
    queryset = Ads.objects.all()
    context_object_name: str = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        """Функция отображения данных в шаблоне общей статистики"""

        context: dict = super(AdsListView, self).get_context_data(**kwargs)
        for ads in self.queryset:
            ads.leads_count = count_of_leads(ads)
            ads.customers_count = count_of_customers(ads)
            ads.profit = profit_ads(ads)
            ads.save()
        return context


class AdsCreateView(CreateView):
    """Создание рекламной кампании"""

    model = Ads
    fields: tuple = 'name', 'product', 'promotion_channel', 'budget'
    success_url = reverse_lazy('ads:ads')

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AdsDeleteView(DeleteView):
    """Удаление рекламной кампании"""

    model = Ads
    success_url = reverse_lazy('ads:ads')


class AdsDetailView(DetailView):
    """Просмотр детальной страницы рекламной кампании"""

    template_name: str = 'ads/ads-detail.html'
    queryset = Ads.objects.all()
    context_object_name: str = 'ads'


class AdsUpdateView(UpdateView):
    """Редактирование рекламной кампании"""

    model = Ads
    fields: tuple = 'name', 'product', 'promotion_channel', 'budget'
    template_name_suffix: str = '_update_form'

    def get_success_url(self) -> str:
        return reverse('ads:ads-detail',
                       kwargs={"pk": self.object.pk})


class AdsStatisticView(ListView):
    """Статистика рекламных кампаний"""

    template_name: str = 'ads/ads-statistic.html'
    queryset = Ads.objects.all()
    context_object_name: str = 'ads'

