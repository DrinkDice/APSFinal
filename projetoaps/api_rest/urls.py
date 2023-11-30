from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_filmes, name='get_all_filmes'),
    path('filme/<str:nome_filme>/', views.get_by_filme),
    path('data/', views.filme_manager),

]
