from django.db import models

# Create your models here.
from django.forms import formset_factory

from users.models import BaseUser


class ModelSchema(models.Model):
    FORMING = "FM"
    SENT_TO_PROCEED = "STP"
    PROCEEDED = "PRD"
    PAID = "PD"
    READY = "RDY"
    CANCEL = "CNC"

    STATUS = (
        (FORMING, "формируется"),
        (SENT_TO_PROCEED, "отправлен в обработку"),
        (PROCEEDED, "обрабатывается"),
        (PAID, "оплачен"),
        (READY, "готов к выдаче"),
        (CANCEL, "отменен"),
    )

    creator = models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name='создатель схемы')
    title = models.CharField(max_length=64, verbose_name='имя схемы')
    time_to_create = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    time_to_update = models.DateTimeField(auto_now=True, verbose_name='обновлена')
    status = models.CharField(choices=STATUS, max_length=3, default=FORMING, verbose_name="статус")
    is_active = models.BooleanField(default=True, verbose_name="активен")

    class Meta:
        ordering = ('-time_to_update',)
        verbose_name = 'схема'
        verbose_name_plural = 'схемы'

    def __str__(self):
        return 'Текущая схема: {}'.format(self.id)

    def get_total_quantity(self):
        items = self.schemachilds.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.schemachilds.select_related()
        return len(items)

    def __str__(self):
        return f'{self.title} ==> {self.creator.username}'


# class DataType(models.Model):
#     slug = models.SlugField(verbose_name='Slug', max_length=50, unique=True)
#     name = models.CharField(max_length=127, verbose_name='Название')
#     shortname = models.CharField(max_length=127, verbose_name='Короткое имя', blank=True)


class Column(models.Model):
    FULLNAME = 'FN'
    INTEGERTYPE = 'INT'
    COMPANYNAME = 'CNM'
    JOBTYPE = 'JT'
    PHONENUMBER = 'PN'

    DATA_TYPES = (
        (FULLNAME, 'Full name'),
        (INTEGERTYPE, 'Integer'),
        (COMPANYNAME, 'Company'),
        (JOBTYPE, 'Job'),
        (PHONENUMBER, 'phone number'),
    )

    # type = models.ForeignKey(DataType, verbose_name='тип данных', on_delete=models.CASCADE, default='1')
    type = models.CharField(choices=DATA_TYPES, max_length=3, default=None, verbose_name='тип')
    model_schema = models.ForeignKey(ModelSchema, related_name='schemachilds', on_delete=models.CASCADE,
                                     verbose_name='схема')

    name = models.CharField(max_length=127, verbose_name='Имя столбца')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество')

    class Meta:
        verbose_name = 'столбец схемы'
        verbose_name_plural = 'столбцы схемы'

    def __str__(self):
        return f'{self.model_schema.title} <== {self.name}'


# ColumnFormSet = formset_factory(Column, extra=1)
