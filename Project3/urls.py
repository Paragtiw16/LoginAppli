"""Project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# import loginform
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.http import request

import loginapp
from loginapp.views import auth, signup, home, otp, login_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^otp/$', otp),
    url(r'^signup/$',signup ),
    url(r'^home/$',home),
    url(r'^auth/$',auth),
    url(r'^login_login/$',login_login)


]
