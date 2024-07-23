from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm, RegisterForm

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm), name='signin'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('profile/', views.profile, name='profile'),
]