"""webkaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('marketplace1.urls')),
        path('auth/', include('authorization.urls')),
        path('auc/', include('auction.urls')),
        path('dialogs/', include('messenger.urls')),
        path('admin1/', include('admin_panel.urls')),

    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# else:
#     urlpatterns = [
#         path('admin/', admin.site.urls),
#         path('', include('marketplace1.urls')),
#         path('auth/', include('authorization.urls')),
#         path('auc/', include('auction.urls')),
#         path('dialogs/', include('messenger.urls')),
#     ]