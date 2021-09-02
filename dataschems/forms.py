
from django.contrib.auth import forms
from django import forms
from dataschems.models import ModelSchema


class ModelSchemaForm(forms.ModelForm):
    class Meta:
        model = ModelSchema
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'




# class ProductAdminUpdateForm(ProductAdminCreationForm):
#     image = forms.ImageField(widget=forms.FileInput(attrs={
#         'class': 'custom-file-input'}), required=False)
#
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'image', 'price', 'quantity', 'category', 'is_active')
