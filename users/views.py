from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from users.forms import UserLoginForm  # UserProfileForm, UserForm
from django.urls import reverse, reverse_lazy
from users.models import BaseUser


# Create your views here.

class UserLogin(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserLogin, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


def user_profile(request):
    return render(request=request, template_name='users/base.html',
                  context={'user': request.user, })


class LogOutUser(LogoutView):
    pass
