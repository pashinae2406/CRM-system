from leads.models import Leads
from customers.models import Customers
from contracts.models import Contracts
from django.db.models import Q


def count_of_leads(ads) -> int:
    """Функция подсчета лидов, узнавших об услуге из данной конкретной рекламной компании"""

    count: int = len([i for i in Leads.objects.filter(ads=ads)])
    return count


def count_of_customers(ads) -> int:
    """Функция подсчета активных клиенетов, узнавших об услуге из конкретной рекламной компании"""

    count: int = len([i for i in Customers.objects.filter(ads=ads)])
    return count


def profit_ads(ads) -> float:
    """Соотношение дохода от контрактов и расходов на рекламу"""

    customers = Customers.objects.filter(ads=ads)
    contracts = Contracts.objects.filter(Q(customer__in=[x.id for x in customers]))
    cost: int = 0
    for contract in contracts:
        cost += contract.cost
    try:
        profit: float = round(cost / ads.budget, 2)
    except ZeroDivisionError:
        profit: float = 0
    return profit
