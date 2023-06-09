import django_filters

from .models import (
    Contract,
    Goods,
    LoanApplicationGoods,
)


__all__ = (
    'ContractFilterSet',
    'GoodsFilterSet',
    'LoanApplicationGoodsFilterSet',
)


class ContractFilterSet(django_filters.FilterSet):

    class Meta:
        model = Contract
        fields = (
            'loan_application',
        )


class GoodsFilterSet(django_filters.FilterSet):

    class Meta:
        model = Goods
        fields = (
            'manufacturer',
        )


class LoanApplicationGoodsFilterSet(django_filters.FilterSet):
    manufacturer = django_filters.NumberFilter(
        field_name='goods__manufacturer',
        lookup_expr='exact',
    )

    class Meta:
        model = LoanApplicationGoods
        fields = (
            'loan_application',
            'manufacturer',
        )
