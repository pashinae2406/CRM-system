from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .models import Ads


class AdsListView(ListView):
    """Список рекламных компаний"""

    template_name = 'ads/ads-list.html'
    queryset = Ads.objects.all()
    context_object_name = 'ads'


class AdsCreateView(CreateView):
    """Создание рекламной кампании"""

    model = Ads
    fields = 'name', 'product', 'promotion_channel', 'budget'
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

    template_name = 'ads/ads-detail.html'
    queryset = Ads.objects.all()
    context_object_name = 'ads'


class AdsUpdateView(UpdateView):
    """Редактирование рекламной кампании"""

    model = Ads
    fields = 'name', 'product', 'promotion_channel', 'budget'
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse('ads:ads-detail',
                       kwargs={"pk": self.object.pk})


class AdsStatisticView(ListView):
    """Статистика рекламных кампаний"""
    template_name = 'ads/ads-statistic.html'
    queryset = Ads.objects.all()
    context_object_name = 'ads'

