from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-tag/', views.add_tag, name='add_tag')
]