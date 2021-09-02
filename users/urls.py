from django.urls import path
from users.views import UserLogin, user_profile, LogOutUser

app_name = 'users'

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
    path('profile/', user_profile, name='profile'),
    path('logout/', LogOutUser.as_view(), name='logout'),
]

