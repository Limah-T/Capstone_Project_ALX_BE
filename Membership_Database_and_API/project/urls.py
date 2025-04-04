"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls import handler400
from rest_framework.authtoken import views
from database.views import custom_404_page
handler400 = custom_404_page

urlpatterns = [
    # Login View for BrowsableAPI
    path("api-auth/", views.obtain_auth_token),
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