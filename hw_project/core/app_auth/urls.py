from django.urls import path, include, reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from core.app_auth import views
from core.app_auth.forms import LoginForm, RegisterForm

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', views.login_view, name='signin'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('profile/', views.profile, name='profile'),
    path('reset_password/', views.CustomPasswordResetView.as_view(
        template_name="app_auth/password_reset.html",
        email_template_name="app_auth/password_reset_email.html",
        success_url=reverse_lazy("app_auth:password_reset_done"),
        ), 
        name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='app_auth/password_reset_done.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='app_auth/password_reset_confirm.html',
        success_url=reverse_lazy('app_auth:password_reset_complete')
        ), 
        name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='app_auth/password_reset_complete.html'), 
        name='password_reset_complete'),
]