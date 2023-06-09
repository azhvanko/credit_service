from rest_framework import serializers

from .models import (
    Contract,
    Goods,
    LoanApplication,
    LoanApplicationGoods,
    Manufacturer,
)


__all__ = (
    'ContractManufacturerSerializer',
    'ContractSerializer',
    'GoodsSerializer',
    'LoanApplicationSerializer',
    'LoanApplicationGoodsSerializer',
    'ManufacturerSerializer',
)


class LoanApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanApplication
        fields = (
            'pk',
            'name',
            'created',
        )


class ContractSerializer(serializers.ModelSerializer):
    loan_application = LoanApplicationSerializer()

    class Meta:
        model = Contract
        fields = (
            'pk',
            'name',
            'loan_application',
            'created',
        )


class ContractManufacturerSerializer(serializers.Serializer):
    manufacturers = serializers.ListSerializer(
        child=serializers.IntegerField(allow_null=False, min_value=1)
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = (
            'pk',
            'name',
            'created',
        )


class GoodsSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Goods
        fields = (
            'pk',
            'name',
            'manufacturer',
            'created',
        )


class LoanApplicationGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = LoanApplicationGoods
        fields = (
            'pk',
            'loan_application',
            'goods',
            'created',
        )
