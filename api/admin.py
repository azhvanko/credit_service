from django.contrib import admin

from .models import (
    Contract,
    Goods,
    LoanApplication,
    LoanApplicationGoods,
    Manufacturer,
)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'get_loan_application_name', 'created',)
    list_filter = ('loan_application__name', 'created',)
    search_fields = ('name',)

    @admin.display(description='Loan application name')
    def get_loan_application_name(self, obj: Contract) -> str:
        return obj.loan_application.name


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'get_manufacturer_name', 'created',)
    list_filter = ('manufacturer__name', 'created',)
    search_fields = ('name',)

    @admin.display(description='Manufacturer name')
    def get_manufacturer_name(self, obj: Goods) -> str:
        return obj.manufacturer.name


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created',)
    list_filter = ('created',)
    search_fields = ('name',)


@admin.register(LoanApplicationGoods)
class LoanApplicationGoodsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_goods_name', 'get_loan_application_name', 'created',)
    list_filter = ('loan_application__name', 'goods__manufacturer', 'created',)
    search_fields = ('name',)

    @admin.display(description='Goods name')
    def get_goods_name(self, obj: LoanApplicationGoods) -> str:
        return obj.goods.name

    @admin.display(description='Loan application name')
    def get_loan_application_name(self, obj: LoanApplicationGoods) -> str:
        return obj.loan_application.name


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created',)
    list_filter = ('created',)
    search_fields = ('name',)
