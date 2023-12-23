"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from igo import views
from igo.views import base_views, comment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('igo/', include('igo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.realindex, name='realindex'),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('', base_views.index1, name='index1'),
    path('', base_views.index2, name='index2'),
    path('', base_views.index3, name='index3'),
    path('', base_views.index4, name='index4'),
    path('', base_views.index5, name='index5'),
    path('', base_views.index7, name='index7'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)