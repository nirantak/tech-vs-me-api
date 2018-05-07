from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:id>/', views.post, name='post'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:id>/', views.author, name='author'),
]
