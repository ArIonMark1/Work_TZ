from django.db import transaction
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from dataschems.forms import ModelSchemaForm, ColumnSchemaForm, ColumnModelFormset
from dataschems.models import ModelSchema, Column


# ==================================================================
class ViewsDataSchema(ListView):
    model = ModelSchema

    def get_queryset(self):
        return ModelSchema.objects.filter(creator=self.request.user)


# ===================================================================
@transaction.atomic
def create_column_with_schema_view(request):
    template_name = 'modelschema_form.html'

    if request.method == 'GET':
        schema_form = ModelSchemaForm(request.GET or None)
        formset = ColumnModelFormset()
    elif request.method == 'POST':
        schema_form = ModelSchemaForm(request.POST)
        formset = ColumnModelFormset(request.POST)

        print(f'{formset}')
        if schema_form.is_valid() and formset.is_valid():
            schema = schema_form.save()
            for form in formset:
                column = form.save(commit=False)
                column.model_schema = schema
                column.save()

            return redirect('users:profile')
    return render(request, template_name, {
        'schema_form': schema_form,
        'formset': formset,

    })


# ===================================================================

# class SchemaColumnCreate(CreateView):
#     template_name = 'modelschema_form.html'
#     model = ModelSchema
#     fields = ['title']
#     success_url = reverse_lazy('schemes:column_create')
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         SchemaFormset = inlineformset_factory(ModelSchema, Column, form=ColumnSchemaForm, extra=1)
#         if self.request.method == 'GET':
#             formset = SchemaFormset(self.request.GET or None)
#         elif self.request.method == 'POST':
#             formset = SchemaFormset(self.request.POST)
#         else:
#             formset = SchemaFormset()
#         data['schemachilds'] = formset
#         return data
#
#     def form_valid(self, form):
#
#         context = self.get_context_data()
#         columns = context['schemachilds']
#
#         with transaction.atomic():
#             form.instance.creator = self.request.user
#             self.object = form.save()
#             if columns.is_valid():
#                 columns.instance = self.object
#                 columns.save()
#             return super(SchemaColumnCreate, self).form_valid(form)


# ==============================================================================

class SchemaDelete(DeleteView):
    model = ModelSchema
    success_url = reverse_lazy('users:profile')
    template_name = 'modelschema_confirm_delete.html'


# ==============================================================================

class SchemaItemsRead(DetailView):
    model = ModelSchema
    form_class = ModelSchemaForm
    template_name = 'modelschema_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'схема/просмотр'
        return context


def order_forming_complete(request, pk):
    order_item = get_object_or_404(ModelSchema, pk=pk)
    order_item.status = ModelSchema.SENT_TO_PROCEED
    order_item.save()

    return HttpResponseRedirect(reverse('users:profile'))
