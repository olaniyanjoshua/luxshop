from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
   path('', views.index, name='index'),
   path('contact/', views.contact, name='contact'),
   path('signup/', views.signup, name='signup'),
   path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
   path('logout/', views.custom_logout, name='logout'),
   path('change-password/', views.change_password, name='change_password'),
   path('change-password-done/', views.password_change_done, name='password_change_done'),
   path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='core/password_reset_form.html',
        email_template_name='core/password_reset_email.html',
        success_url=reverse_lazy('core:password_reset_done')
    ), name='password_reset'),
   path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html', success_url=reverse_lazy('core:password_reset_complete')), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_complete'),
]
