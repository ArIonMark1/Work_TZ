# Generated by Django 3.2.6 on 2021-09-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataschems', '0008_auto_20210908_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='type',
            field=models.CharField(choices=[('FN', 'Full name'), ('INT', 'Integer'), ('CNM', 'Company'), ('JT', 'Job')], default=None, max_length=3, verbose_name='тип поля'),
        ),
        migrations.DeleteModel(
            name='DataType',
        ),
    ]