from django.conf.urls import url


from ajaxlogin.views import signup, home, login_login, auth

urlpatterns = [


    url(r'^signup/$',signup ),
    # url(r'^otp_page/$',otp_page),
    url(r'^home/$',home),
    url(r'^login_login/$',login_login),
    url(r'^auth/$',auth)

    ]