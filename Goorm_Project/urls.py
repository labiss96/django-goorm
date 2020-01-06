from django.contrib import admin
from django.urls import path, include
import main.views
import accounts.views
import goorm.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('goorm/', include('goorm.urls')),
]
