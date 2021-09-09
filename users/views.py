from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import ListView

import dataschems.models
from users.forms import UserLoginForm
from users.models import BaseUser
from dataschems.models import ModelSchema


# Create your views here.

class UserLogin(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserLogin, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class UserProfileView(ListView):
    template_name = 'users/base.html'
    model = BaseUser

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['schemas'] = ModelSchema.objects.filter(creator=self.request.user)
        return context



class LogOutUser(LogoutView):
    pass
