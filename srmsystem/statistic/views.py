from django.views.generic import ListView
from ads.models import Ads
from services.models import Service
from leads.models import Leads
from customers.models import Customers


class StatisticView(ListView):
    """Просмотр общей статистики"""

    template_name: str = 'statistic/index.html'
    queryset: int = len(Ads.objects.all())

    def get_context_data(self, **kwargs) -> dict:
        """Функция для отображения данных статистики в шаблоне"""

        context: dict = super(StatisticView, self).get_context_data(**kwargs)
        context['advertisements_count'] = len(Ads.objects.all())
        context['products_count'] = len(Service.objects.all())
        context['leads_count'] = len(Leads.objects.all())
        context['customers_count'] = len(Customers.objects.all())
        return context
