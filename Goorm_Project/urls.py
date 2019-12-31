from django.contrib import admin
from django.urls import path, include
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
