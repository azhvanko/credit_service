import logging

from django.db.models import QuerySet
from django.http.response import Http404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import (
    ContractFilterSet,
    GoodsFilterSet,
    LoanApplicationGoodsFilterSet,
)
from .models import (
    Contract,
    Goods,
    LoanApplication,
    LoanApplicationGoods,
    Manufacturer,
)
from .serializers import (
    ContractManufacturerSerializer,
    ContractSerializer,
    GoodsSerializer,
    LoanApplicationSerializer,
    LoanApplicationGoodsSerializer,
    ManufacturerSerializer,
)


__all__ = (
    'ContractView',
    'GoodsView',
    'LoanApplicationView',
    'LoanApplicationGoodsView',
    'ManufacturerView',
)


logger = logging.getLogger(__name__)


class ContractView(ModelViewSet):
    authentication_classes = ()  # TODO
    serializers = {
        'default': ContractSerializer,
    }
    http_method_names = ('get', 'post', 'patch', 'head', 'delete',)
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filterset_class = ContractFilterSet
    search_fields = ('name',)

    def get_queryset(self) -> QuerySet:
        if getattr(self, 'swagger_fake_view', False):
            return Contract.objects.none()
        return Contract.objects.select_related('loan_application').all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    @swagger_auto_schema(
        responses={
            200: ContractManufacturerSerializer(),
        },
    )
    @action(methods=['get'], detail=True)
    def manufacturer(self, request, *args, **kwargs) -> Response:  # noqa
        loan_application_qs = Contract.objects.values('loan_application').filter(**self.kwargs)
        qs = (
            LoanApplicationGoods.objects
                .filter(loan_application__in=loan_application_qs)
                .select_related('goods')
                .values_list('goods__manufacturer', flat=True)
                .order_by()
                .distinct()
        )
        if not qs:
            raise Http404
        output_serializer = ContractManufacturerSerializer(data={'manufacturers': qs, })
        output_serializer.is_valid(raise_exception=False)
        return Response(data=output_serializer.data)


class GoodsView(ModelViewSet):
    authentication_classes = ()  # TODO
    serializers = {
        'default': GoodsSerializer,
    }
    http_method_names = ('get', 'post', 'patch', 'head', 'delete',)
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filterset_class = GoodsFilterSet
    search_fields = ('name',)

    def get_queryset(self) -> QuerySet:
        if getattr(self, 'swagger_fake_view', False):
            return Goods.objects.none()
        return Goods.objects.select_related('manufacturer').all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])


class LoanApplicationView(ModelViewSet):
    authentication_classes = ()  # TODO
    serializers = {
        'default': LoanApplicationSerializer,
    }
    http_method_names = ('get', 'post', 'patch', 'head', 'delete',)
    filter_backends = (
        SearchFilter,
    )
    search_fields = ('name',)

    def get_queryset(self) -> QuerySet:
        if getattr(self, 'swagger_fake_view', False):
            return LoanApplication.objects.none()
        return LoanApplication.objects.all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])


class LoanApplicationGoodsView(ModelViewSet):
    authentication_classes = ()  # TODO
    serializers = {
        'default': LoanApplicationGoodsSerializer,
    }
    http_method_names = ('get', 'post', 'patch', 'head', 'delete',)
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_class = LoanApplicationGoodsFilterSet

    def get_queryset(self) -> QuerySet:
        if getattr(self, 'swagger_fake_view', False):
            return LoanApplicationGoods.objects.none()
        return (
            LoanApplicationGoods.objects
                .select_related('goods', 'goods__manufacturer', 'loan_application')  # noqa
                .all()
        )

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])


class ManufacturerView(ModelViewSet):
    authentication_classes = ()  # TODO
    serializers = {
        'default': ManufacturerSerializer,
    }
    http_method_names = ('get', 'post', 'patch', 'head', 'delete',)
    filter_backends = (
        SearchFilter,
    )
    search_fields = ('name',)

    def get_queryset(self) -> QuerySet:
        if getattr(self, 'swagger_fake_view', False):
            return Manufacturer.objects.none()
        return Manufacturer.objects.all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])
