"""demoauthenti URL Configuration

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
from signup.views import sign,user_login,user_profile,user_logout,user_change_pass,user_change_pass1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',sign),
    path('login/',user_login),
    path('profile/',user_profile,name='profile'),
    path('logout/',user_logout,name='logout'),
    path('passchange/',user_change_pass,name='passchange'),
    path('passchange1/',user_change_pass1,name='passchange1')

]
