from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from dataschems.forms import ModelSchemaForm, ColumnSchemaForm
from dataschems.models import ModelSchema, Column


# Create your views here.
# ==================================================================
class ViewsDataSchema(ListView):
    model = ModelSchema

    def get_queryset(self):
        return ModelSchema.objects.filter(creator=self.request.user)


# ===================================================================

class SchemaColumnCreate(CreateView):
    model = ModelSchema
    form_class = ModelSchemaForm
    template_name = 'modelschema_form.html'
    success_url = reverse_lazy('schemes:column_create')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        SchemaFormset = inlineformset_factory(ModelSchema, Column, form=ColumnSchemaForm, extra=1)

        if self.request.method == 'POST':
            formset = SchemaFormset(self.request.POST)
        else:
            formset = SchemaFormset()
        data['schemachilds'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        columns = context['schemachilds']

        with transaction.atomic():
            form.instance.creator = self.request.user
            self.object = form.save()
            if columns.is_valid():
                columns.instance = self.object
                columns.save()
            return super(SchemaColumnCreate, self).form_valid(form)


# ==============================================================================

@login_required()
def schema_remove(request, b_id):
    ModelSchema.objects.get(id=b_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
