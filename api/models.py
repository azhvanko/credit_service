from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'
        db_table = 'manufacturer'

    def __str__(self) -> str:
        return str(self.name)


class Goods(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='manufacturer',
        db_column='manufacturer',
    )
    name = models.CharField(max_length=256)
    created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'goods'
        verbose_name_plural = 'goods'
        db_table = 'goods'

    def __str__(self) -> str:
        return str(self.name)


class LoanApplication(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'loan_application'
        verbose_name_plural = 'loan_applications'
        db_table = 'loan_application'

    def __str__(self) -> str:
        return str(self.name)


class LoanApplicationGoods(models.Model):
    goods = models.OneToOneField(
        Goods,
        on_delete=models.CASCADE,
        related_name='goods',
        db_column='goods',
        primary_key=True,
    )
    loan_application = models.ForeignKey(
        LoanApplication,
        on_delete=models.CASCADE,
        related_name='loan_application_goods',
        db_column='loan_application',
    )
    created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        ordering = (
            '-created',
            'loan_application',
        )
        verbose_name = 'loan_application_goods'
        verbose_name_plural = 'loan_applications_goods'
        db_table = 'loan_application_goods'

    def __str__(self) -> str:
        return str(self.goods)


class Contract(models.Model):
    loan_application = models.OneToOneField(
        LoanApplication,
        on_delete=models.CASCADE,
        related_name='loan_application_contract',
        db_column='loan_application',
    )
    name = models.CharField(max_length=256)
    created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'contract'
        verbose_name_plural = 'contracts'
        db_table = 'contract'

    def __str__(self) -> str:
        return str(self.name)
