from django.urls import path, re_path
from . import views

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('access_denied/', views.access_denied, name='access_denied'),

    # ... Reseteo de contraseña ...

    path('password-reset/',
         PasswordResetView.as_view(
             template_name='accounts/registration/password_reset.html',
             html_email_template_name='accounts/registration/password_reset_email.html'
         ),
         name='password-reset'
         ),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='accounts/registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='accounts/registration/password_reset_complete.html'), name='password_reset_complete'),
]