from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('portal',views.portal),
    path('donate',views.donate),
    path('learnaboutdonation',views.learnaboutdonation),
    path('profile/',views.userprofile),
    path('mydonations/',views.mydonations),
    path('event/',views.events),
]