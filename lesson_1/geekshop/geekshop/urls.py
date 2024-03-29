"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ('', mainapp.main, name='main'),
    path ('contact/', mainapp.contact, name='contact'),
    path ('products/', include('mainapp.urls', namespace='products')),
    path ('molinezia/', mainapp.molinezia, name='molinezia'),
    path ('neon/', mainapp.neon, name='neon'),
    path ('pecilia/', mainapp.pecilia, name='pecilia'),
    path ('auth/', include('authapp.urls', namespace='auth')),
    path ('admin/', admin.site.urls),
    path ('basket/', include('basketapp.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)