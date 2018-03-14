from django.http import request
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import random
from django.views.decorators.csrf import csrf_exempt

# from ajaxlogin.models import Login
from ajaxlogin.models import Logins


@csrf_exempt
def signup(request):

    if request.method=="GET":
        return render(request, "signup1.html")

    elif request.method=="POST":
        print("inside signup POST Method")
        get_uname=request.POST.get('name')
        get_pwd=request.POST.get('password')
        get_email=request.POST.get('Email')
        get_number =request.POST.get('no')
        print("get_uname ", get_uname)
        print("get_email ", get_email)
        # global  get_uname,get_pwd,get_number,get_email
        for x in range(1000):
            global otp
            otp = random.randint(1, 21) * 5
            break
            print(otp)

            # email = EmailMessage('Subject', otpname, to=['get_email'])
            # email.send()
        from django.core.mail import send_mail
        send_mail('test email', str(otp), 'Paragtiwari314@gmail.com', [get_email])


        # key = 'secret'
        # encoded = jwt.encode({'pwd': 'get_pwd'}, key, algorithm='HS256')
        # decoded = jwt.decode(encoded, key, algorithms='HS256')
        # {'pwd': 'get_pwd'}\
        try:

            login_details = Logins.objects.create(username=get_uname,password= get_pwd,
                                                         email= get_email,contactno=get_number)
            # login_details.save()
        except Exception,e:
            print("Our Error=",str(e))
        # login_details =Login(username=get_uname,password= password,email= email)
        # login_details.save()
        print("Number=",get_number)
        # JSON={"Email": get_email}
        # print("JJJJJJJJJJJJJSSSSSSSSSSSSOOOOONNNNN=",JSON)
        return render(request, "otp1.html", {"Email": get_email})




# @csrf_exempt
# def otp_page(request):
#     if request.method == "POST":
#         print('qwertyu')
#         get_uname=request.POST.get('name')
#         get_pwd=request.POST.get('password')
#         get_email=request.POST.get('Email')
#         get_number =request.POST.get('no')
#         global  get_uname,get_pwd,get_number,get_email
#         for x in range(1000):
#             global otp
#             otp = random.randint(1, 21) * 5
#             break
#
#             # email = EmailMessage('Subject', otpname, to=['get_email'])
#             # email.send()
#         from django.core.mail import send_mail
#         send_mail('test email', str(otp), 'Paragtiwari314@gmail.com', [get_email])
#
#
#         # key = 'secret'
#         # encoded = jwt.encode({'pwd': 'get_pwd'}, key, algorithm='HS256')
#         # decoded = jwt.decode(encoded, key, algorithms='HS256')
#         # {'pwd': 'get_pwd'}
#         login_details = Login.objects.create(username=get_uname,password= get_pwd,email= get_email
#                                              ,contactno=get_number)
#         # login_details =Login(username=get_uname,password= password,email= email)
#         login_details.save()parag11
#
#         return render(request, "otp1.html", {"Email":get_email})
@csrf_exempt
def home(request):
     if request.method=="POST":
         get_otp=request.POST.get('Otp')
         if(get_otp==str (otp)):
             # data = Login.objects.all()
             # for i in data:
             #     user = (i.username)get_un
             #     pssword = (i.password)
             #     print(pssword)
             #     email = (i.email)
             #     print(email)
             #     no = (i.contactno)
                 return render(request, "home1.html")
             # {"Username": get_uname,
             #  "Email": get_email, "Contact_no": get_number}
         else:
             msg="Please enter correct otp"

             return render(request, "otp1.html",{"Message":msg})
@csrf_exempt
def login_login(request):
    return render(request,"Login.html")
@csrf_exempt
def auth(request):
     if request.method=="POST":
         data = Logins.objects.all()
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
         get_email=request.POST.get('Email')
         get_pswd=request.POST.get('Password')
         # get_number=request.POST.get(no)
         if email==get_email and pssword==get_pswd:
             print("true")
             return render(request, "home1.html",{"Username":user,"Email":email,
                                                                        "Contact_no":no} )
         else:
             msg="Please enter Correct Details"
             return render(request, "Login1.html",{"Message":msg})
