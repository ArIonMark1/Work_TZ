import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from dataschems.models import ModelSchema

# class ProductAdminUpdateForm(ProductAdminCreationForm):
#     image = forms.ImageField(widget=forms.FileInput(attrs={
#         'class': 'custom-file-input'}), required=False)
#
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'image', 'price', 'quantity', 'category', 'is_active')
