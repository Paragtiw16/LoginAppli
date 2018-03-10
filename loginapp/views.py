# from django.shortcuts import render

# Create your views here.
# import password as password
# from django.http import request
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# import render as render
# from random import random

import jwt
from django.core.mail.message import EmailMessage
from django.shortcuts import render
from django.utils.crypto import random
from django.views.decorators.csrf import csrf_exempt

from loginapp.models import Login


@csrf_exempt
def loginreq(request):
    if request.method == "POST":
        get_uname=request.POST.get('uname')
        get_pwd=request.POST.get('pwd')
        get_email=request.POST.get('email')
        get_number =request.POST.get('number')
        for x in range(1000):
            otp = random.randint(1, 21) * 5
            break

            # email = EmailMessage('Subject', otp, to=['get_email'])
            # email.send()
        from django.core.mail import send_mail
        send_mail('test email', str(otp), 'Paragtiwari314@gmail.com', ['shivam.mittal38@gmail.com'])


        key = 'secret'
        encoded = jwt.encode({'pwd': 'get_pwd'}, key, algorithm='HS256')
        decoded = jwt.decode(encoded, key, algorithms='HS256')
        {'pwd': 'get_pwd'}
        login_details = Login.objects.create(username=get_uname,password= encoded,email= get_email
                                             ,contactno=get_number)
        # login_details =Login(username=get_uname,password= password,email= email)
        login_details.save()

        return render(request, "login.html")

def loginform(request):

     if request.method=="GET":
        return render(request, "signup.html")



def login_reqq(request):
     if request.method=="GET":
         return render(request,"match.html")


@csrf_exempt
def auth(request):
     if request.method=="POST":
         data = Login.objects.all()
         for i in data:
             user=(i.username)
             pssword =(i.password)
             email=(i.email)
             no=(i.contactno)
             print(user)
         # user= data.username
         # pssword =data.password
         # email=data.email
         get_pwd=request.POST.get('pwd')
         get_email=request.POST.get('email')
         get_number=request.POST.get(no)
         if pssword==get_pwd and email==get_email and (no==get_number):
            return render(request, "user.html" ,{"Username":user})


