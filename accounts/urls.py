from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.acc_signup, name='acc_signup'),
    path('login/', views.acc_login, name='acc_login'),
    path('logout/', views.acc_logout, name='acc_logout'),

]
