from django.contrib import admin
from django.urls import path
from . import views #importing views from the current directory

urlpatterns = [
    path('', views.index, name='home')
]