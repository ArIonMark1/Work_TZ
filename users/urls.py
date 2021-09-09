from django.urls import path
from users.views import UserLogin, LogOutUser, UserProfileView

app_name = 'users'

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogOutUser.as_view(), name='logout'),
]

