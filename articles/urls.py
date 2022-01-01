from django.urls import path
from . import views
from random import randint


urlpatterns = [

    path('', views.articles_home, name='articles_home'),
    path('artcl=<slug:slug>/', views.articles_details, name='articles_details'),
    path('create/', views.articles_create, name='articles_create'),


]