# Generated by Django 3.2.6 on 2021-08-12 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=127, verbose_name='Название')),
                ('shortname', models.CharField(blank=True, max_length=127, verbose_name='Короткое имя')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название записи')),
                ('description', models.TextField(blank=True, max_length=400, verbose_name='Анонс')),
                ('type', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dataschems.DataType', verbose_name='тип данных')),
            ],
        ),
    ]