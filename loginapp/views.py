# from django.shortcuts import render

# Create your views here.
# import password as password
# from django.http import request
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# import render as render
# from random import random
import json

import jwt
from django.core.mail.message import EmailMessage
from django.shortcuts import render
from django.utils.crypto import random
from django.views.decorators.csrf import csrf_exempt

from loginapp.models import Login


@csrf_exempt
def otp(request):
    if request.method == "POST":
        get_uname=request.POST.get('uname')
        get_pwd=request.POST.get('pwd')
        get_email=request.POST.get('email')
        get_number =request.POST.get('number')
        global  get_uname,get_pwd,get_number,get_email
        for x in range(1000,9999):
            global otp
            otp = random.randint(1000,9999)
            break


        from django.core.mail import send_mail
        send_mail('Your OTP is', str(otp), 'Paragtiwari314@gmail.com', [get_email])


        key = 'secret'
        encoded = jwt.encode({'pwd': get_pwd}, key, algorithm='HS256')
        # decoded = jwt.decode(encoded, key, algorithms='HS256')
        {'pwd': 'get_pwd'}
        login_details = Login.objects.create(username=get_uname,password= encoded,email= get_email
                                             ,contactno=get_number)
        # login_details =Login(username=get_uname,password= password,email= email)
        login_details.save()

        return render(request, "otp.html", {"Email":get_email})

@csrf_exempt
def signup(request):

     if request.method=="GET":
        return render(request, "signup.html")


@csrf_exempt
def home(request):
     if request.method=="POST":
         get_otp=request.POST.get('otp')
         if(get_otp==str (otp)):
             # data = Login.objects.all()
             # for i in data:
             #     user = (i.username)get_un
             #     pssword = (i.password)
             #     print(pssword)
             #     email = (i.email)
             #     print(email)
             #     no = (i.contactno)
                 return render(request, "home.html", {"Username":get_uname,
                                             "Email":get_email,"Contact_no":get_number})
         else:
             msg="Please enter correct otp"

             return render(request, "otp.html",{"Message":msg})






@csrf_exempt
def auth(request):
     if request.method=="POST":
         data = Login.objects.all()
         for i in data:
             email=(i.email)
             pssword =(i.password)
             user=(i.username)
             # decoded = jwt.decode(pssword, 'secret', algorithms='HS256')
             #  email=(i.email)
             no=(i.contactno)
         # user= data.username
         # pssword =data.password
         # email=data.email
         get_email=request.POST.get('email')
         get_pswd=request.POST.get('pwd')
         key = 'secret'
         encoded = jwt.encode({'pwd': get_pswd}, key, algorithm='HS256')
         # get_number=request.POST.get(no)
         print(pssword)
         print(encoded)
         if email==get_email and pssword==encoded:
             print("true")
             print(email)
             print(get_email)

             return render(request, "home.html",{"Username":user,"Email":email,
                                                                        "Contact_no":no} )
         else:
             msg="Please enter Correct Details"
             return render(request, "Login.html",   {"Message":msg})



@csrf_exempt
def login_login(request):
    return render(request,"Login.html")

def recovery(request):
    # print("HHHHHEEEEEEEEEEELLLLLLLLLLLLLLLLLOOOOO")
    # if request.method=="GET":
    #     get_email = request.GET.get('email')
    #     print("MERA EMAIL=",get_email)
    #     obj = Login.objects.get(Email=get_email)
    #     password=obj.Password
    #     print(password)
    #     from django.core.mail import send_mail
    #     send_mail('test email', password, 'Paragtiwari314@gmail.com', [get_email])
    #
    #     return render(request, "Login.html")

      return render(request, "Forgot.html")

@csrf_exempt
def password(request):
    print("HHHHHEEEEEEEEEEELLLLLLLLLLLLLLLLLOOOOO")
    if request.method == "POST":
        get_email = request.POST.get('email')
        print("MERA EMAIL=", get_email)
        obj = Login.objects.get(email=get_email)
        Password = obj.password
        print(Password)
        key = 'secret'
        # encoded = jwt.encode({'pwd': get_pwd}, key, algorithm='HS256')
        decoded = jwt.decode(Password, key, algorithms='HS256')
        print("`Mera Password=",decoded)
        # d=({u'pwd': u'ppoiuyt'})
        # var=json.loads('{"pwd":decoded}')
        var=decoded['pwd']


        print("Password==========",var)
        # d = {'pwd': decoded}

        # for key, value in d.items():
        #
        #        print key, value
        try:

            from django.core.mail import send_mail
            send_mail('test email', var, 'Paragtiwari314@gmail.com', [get_email])
        except Exception, e:
            print("Apna  Error=", str(e))

        return render(request, "Login.html")







