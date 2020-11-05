"""djangoProject URL Configuration

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
from django.urls import path
from static import views as st_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', st_view.index),
    path('event/<int:pk>', st_view.event, name='event'),
    path('home/<int:pk>', st_view.home, name='home'),
    path('register/', st_view.register, name='reg'),
    path('login/', st_view.login, name='log'),
    path('review/', st_view.review, name='review'),
    path('postissue/', st_view.post_issue, name='pos'),
    path('segmentation/', st_view.segmentation, name='seg'),
    path('map/<int:pk>', st_view.map, name='map'),
    path('mappo/<int:id>/<int:pk>', st_view.mapop, name='mappo'),
]
