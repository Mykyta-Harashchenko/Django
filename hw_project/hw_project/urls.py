from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('quotes.urls')),
    path('auth/', include('app_auth.urls')),
    path('admin/', admin.site.urls)
]
