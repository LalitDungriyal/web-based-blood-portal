from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('services/',views.services),
    path('gallary/',views.gallary),
    path('about/',views.about),
]