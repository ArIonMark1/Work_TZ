from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django import forms
from users.models import BaseUser, Profile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))

    class Meta:
        model = BaseUser
        fields = ('username', 'password',)


# === === === === === === === === === === === === ===
# class UserForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'Username', 'readonly': True,
#     }))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'First Name',
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'Last Name',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Email', 'readonly': True,
#     }))
#     class Meta:
#         model = BaseUser
#         fields = ('username', 'first_name', 'last_name', 'email',)
#
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
