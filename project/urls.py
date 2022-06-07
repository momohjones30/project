"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from argparse import Namespace
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from quizes import views
from main import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quizes.urls', namespace='quizes')),
    path('', include('main.urls', namespace='main')),
    # path('', include('main.urls', namespace='stafflogin')),
    # path('', include('main.urls', namespace='studentlogin'))
]
admin.site.index_title = 'Dashboard'
admin.site.site_header = 'Friendswood Administration'
admin.site.site_title = 'Friendswood Administration'






urlpatterns += static(settings.STATIC_URL, Document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()