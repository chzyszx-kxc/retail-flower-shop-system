# Django 依赖
from django.urls import path

# 当前应用依赖
from accounts.views import (
    CsrfCookieView,
    CurrentUserView,
    LoginView,
    LogoutView,
)


app_name = 'accounts'

urlpatterns = [
    path(
        'csrf/',
        CsrfCookieView.as_view(),
        name='csrf',
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login',
    ),
    path(
        'me/',
        CurrentUserView.as_view(),
        name='current-user',
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout',
    ),
]