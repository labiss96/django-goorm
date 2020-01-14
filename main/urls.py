from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('buy_tobacco',views.buy_tobacco, name = 'buy_tobacco'),
    path('save_log',views.save_log, name = 'save_log'),
]
