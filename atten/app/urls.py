from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('handleLogout',views.handleLogout,name='handleLogout'),
    path('about',views.about,name='about'),
    path('uploadcsv',views.uploadcsv,name='uploadcsv'),
    path('attendance',views.attendance,name='attendance'),
]