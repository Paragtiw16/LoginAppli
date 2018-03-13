from django.conf.urls import url

from loginapp.views import signup, otp, home, login_login, auth

urlpatterns = [


    url(r'^signup/$',signup ),
    url(r'^otp/',otp),
    url(r'^home/$',home),
    url(r'^login_login/$',login_login),
    url(r'^auth/$',auth)

    ]