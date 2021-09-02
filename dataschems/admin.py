from django.contrib import admin

# Register your models here.
from dataschems.models import DataType, ModelSchema, Column

admin.site.register(DataType)
admin.site.register(ModelSchema)
admin.site.register(Column)

