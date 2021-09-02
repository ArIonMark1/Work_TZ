from django.db import models

# Create your models here.
from users.models import BaseUser


class ModelSchema(models.Model):
    creator = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    time_to_create = models.DateTimeField(auto_now_add=True)


class DataType(models.Model):
    slug = models.SlugField(verbose_name='Slug', max_length=50, unique=True)
    name = models.CharField(max_length=127, verbose_name='Название')
    shortname = models.CharField(max_length=127, verbose_name='Короткое имя', blank=True)


class Column(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название записи')
    description = models.TextField(max_length=400, verbose_name='Анонс', blank=True)

    type = models.ForeignKey(DataType, verbose_name='тип данных', on_delete=models.CASCADE, default='1')
    model = models.ForeignKey(ModelSchema, verbose_name='Таблица', on_delete=models.CASCADE)
