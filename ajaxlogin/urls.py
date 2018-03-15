from django.conf.urls import url


from ajaxlogin.views import signup, login_login, auth, otppage, home

urlpatterns = [


    url(r'^signup/$',signup ),
     url(r'^otppage/$',otppage),
     url(r'^home/$',home),
    url(r'^login_login/$',login_login),
    url(r'^auth/$',auth)

    ]