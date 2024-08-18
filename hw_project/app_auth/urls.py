from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from . import views
from .forms import LoginForm, RegisterForm

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm), name='signin'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('profile/', views.profile, name='profile'),
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]