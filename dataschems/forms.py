from django.contrib.auth import forms
from django import forms
from django.forms import formset_factory, modelformset_factory, inlineformset_factory

from dataschems.models import ModelSchema, Column


class ModelSchemaForm(forms.ModelForm):
    class Meta:
        model = ModelSchema
        exclude = 'creator', 'is_active',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ColumnSchemaForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = 'name', 'type', 'quantity',

    def __init__(self, *args, **kwargs):
        super(ColumnSchemaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# ColumnFormSet = formset_factory(ColumnSchemaForm, extra=1)

# ColumnModelFormset = modelformset_factory(
#     Column,
#     form=ColumnSchemaForm,
#     fields=('name', 'type', 'quantity',),
#     extra=1
# )
ColumnModelFormset = inlineformset_factory(
    ModelSchema,
    Column,
    form=ColumnSchemaForm,
    fields=('name', 'type', 'quantity',),
    extra=1,
)

# ColumnFormset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
