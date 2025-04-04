from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls import handler400
from database import views

# Handles 404 page
handler400 = views.custom_404_page

urlpatterns = [
    path('', RedirectView.as_view(url='database/home', permanent=True)),
    path('admin/', admin.site.urls, name='admin'),
    path('database/', include('database.urls')),
    path('api/', include('api.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    print(True)
    print(settings.MEDIA_URL, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)