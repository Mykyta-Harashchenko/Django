from django.urls import path

from core.quotes import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-tag/', views.add_tag, name='add_tag'),
    path('author/<int:author_id>', views.author_info, name='author_info'),
    path('search/', views.search_quotes, name='search'),
    path('random-quote/', views.random_quote, name='random_quote'),
    path('like/<int:quote_id>/', views.like_quote, name='like_quote'),
    path('tag/<int:tag_id>', views.quotes_by_tag, name='tag_info')
]