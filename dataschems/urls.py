from django.urls import path

from dataschems.views import ViewsDataSchema, SchemaColumnCreate, schema_remove


app_name = 'schemes'

urlpatterns = [
    path('', ViewsDataSchema.as_view(), name='schemes_list'),
    path('add/', SchemaColumnCreate.as_view(), name='column_create'),


    # path('remove/<int:b_id>/', schema_remove, name='schema_remove'),
]

