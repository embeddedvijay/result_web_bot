"""
URL configuration for smart_matka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from reader import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index,name='index'),
    path('admin/', admin.site.urls),
    path('group_automatic_bot', views.group_automatic_bot,name='test'),
    path('login/', views.login, name='login'),
    path('admin_loging', csrf_exempt(views.admin_loging), name='admin_loging'),
    path('add_group_result', csrf_exempt(views.add_group_result), name='add_group_result'),
    path('add_personal_result', csrf_exempt(views.add_personal_result), name='add_personal_result'),
    path('configure_market_time', csrf_exempt(views.configure_market_time), name='configure_market_time'),
    path('update_market_time', csrf_exempt(views.update_market_time), name='update_market_time'),
    
]
