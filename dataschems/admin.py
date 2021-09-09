from django.contrib import admin

# Register your models here.
from dataschems.models import ModelSchema, Column

admin.site.register(ModelSchema)
admin.site.register(Column)

