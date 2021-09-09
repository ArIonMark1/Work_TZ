from django.contrib.auth import forms
from django import forms
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
