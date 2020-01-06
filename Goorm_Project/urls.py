from django.contrib import admin
from django.urls import path, include
import main.views
import accounts.views
import goorm.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('goorm/', include('goorm.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)