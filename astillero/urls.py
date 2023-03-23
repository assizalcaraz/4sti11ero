"""astillero URL Configuration

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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # URL raíz del sitio
    path('', include('users.urls')), # aplicación de usuarios
    #path('store/', include('store.urls')), # aplicación de tienda
    #path('blog/', include('blog.urls')), # aplicación de blog
    #path('elearning/', include('elearning.urls')), # aplicación de elearning
    #path('comun/', include('comun.urls')), # aplicación de comunidad
    # otras rutas aquí ...

    
]