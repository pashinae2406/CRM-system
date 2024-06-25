from django.views.generic import ListView
from ads.models import Ads
from services.models import Service
from leads.models import Leads
from customers.models import Customers


class StatisticView(ListView):
    """Просмотр общей статистики"""

    template_name = 'statistic/index.html'
    queryset = len(Ads.objects.all())
    context_object_name = 'advertisements_count'

    def get_context_data(self, **kwargs):
        context = super(StatisticView, self).get_context_data(**kwargs)
        context['products_count'] = len(Service.objects.all())
        context['leads_count'] = len(Leads.objects.all())
        context['customers_count'] = len(Customers.objects.all())
        return context
