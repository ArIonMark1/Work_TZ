from django.urls import path

from dataschems.views import ViewsDataSchema, SchemaDelete, create_column_with_schema_view, SchemaItemsRead


app_name = 'schemes'

urlpatterns = [
    path('', ViewsDataSchema.as_view(), name='schemes_list'),
    path('add/', create_column_with_schema_view, name='column_create'),


    path('read/<pk>/', SchemaItemsRead.as_view(), name='read'),
    path('delete/<pk>/', SchemaDelete.as_view(), name='delete'),
    # path('remove/<int:b_id>/', schema_remove, name='schema_remove'),
]

