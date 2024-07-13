from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.index, name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout')

]