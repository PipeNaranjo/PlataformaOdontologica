"""SandraOrozco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include

authUrl='django.contrib.auth.urls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SandraOrozcoApp.urls')),
    path('informacion/',include('informacion.urls')),
    path('citas/', include('citas.urls')),
    path('contactanos',include('contactanos.urls')),
    path('accounts/', include(authUrl)),
    path('accounts/logout/',include(authUrl),name='logout'),
    path('accounts/password_change/',include(authUrl),name='password_change'),
    path('accounts/password_change/done/',include(authUrl),name='password_change_done'),
    path('accounts/password_reset/',include(authUrl),name='password_reset'),
    path('accounts/password_reset/done/',include(authUrl), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',include(authUrl),name='password_reset_confirm'),
    path('accounts/reset/done/',include(authUrl), name='password_reset_complete'),
    path('accounts/login/',include(authUrl),name='login'),
]
