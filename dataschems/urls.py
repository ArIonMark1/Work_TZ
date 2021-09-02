from django.urls import path

from dataschems.views import schema_views, schema_edit, ModelSchemaCreateView, schema_remove


app_name = 'schemes'

urlpatterns = [
    path('', schema_views, name='schemes'),

    path('add/', ModelSchemaCreateView.as_view(), name='schema_add'),
    path('remove/<int:b_id>/', schema_remove, name='schema_remove'),
    path('edit/<int:p_id>/<int:quantity>/', schema_edit, name='schema_edit'),
]

