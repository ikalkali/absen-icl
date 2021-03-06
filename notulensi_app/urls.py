"""notulensi URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/rapat', views.rapat_list.as_view()),
    path('api/absen', views.absensi_list.as_view()),
    path('api/asisten', views.asisten_list.as_view()),
    path('api/detail-hadir/<int:pk>', views.hadir_list.as_view()),
    path('api/detail-absen/<int:pk>', views.tidak_hadir_list.as_view()),
    path('api/asisten/<str:nim>', views.detail_asisten.as_view()),
]
