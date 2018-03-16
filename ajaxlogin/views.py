from django.http import request
from django.shortcuts import render, render_to_response

# Create your views here.
from django.utils.crypto import random
from django.views.decorators.csrf import csrf_exempt

# from ajaxlogin.models import Login
from ajaxlogin.models import Logins
from ajaxlogin.models import New
from django.http import JsonResponse
@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, "signup1.html")

    elif request.method == "POST":
        print("inside signup POST Method")
        get_uname = request.POST.get('name')
        get_pwd = request.POST.get('password')
        get_email = request.POST.get('Email')
        get_number = request.POST.get('no')
        print("get_uname ", get_uname)
        print("get_email ", get_email)
        # global  get_uname,get_pwd,get_number,get_email
        for x in range(1000,9999):
            # global otp
            Otp = random.randint(1000,9999)
            break
            print(Otp)

            # email = EmailMessage('Subject', otpname, to=['get_email'])
            # email.send()
        from django.core.mail import send_mail
        send_mail('test email', str(Otp), 'Paragtiwari314@gmail.com', [get_email])

        # key = 'secret'
        # encoded = jwt.encode({'pwd': 'get_pwd'}, key, algorithm='HS256')
        # decoded = jwt.decode(encoded, key, algorithms='HS256')
        # {'pwd': 'get_pwd'}\
        try:

            login_details = Logins.objects.create(username=get_uname, password=get_pwd,
                                                  email=get_email, contactno=get_number)
            match_details=New.objects.create(otp=Otp,new=login_details)

            
            # login_details.save()

        except Exception, e:
            print("Our Error=", str(e))
        # login_details =Login(username=get_uname,password= password,email= email)
        # login_details.save()
        print("Number=", get_number)
        # JSON={"Email": get_email}
        # print("JJJJJJJJJJJJJSSSSSSSSSSSSOOOOONNNNN=",JSON)
        #   return render(request, "otp1.html", {"Email": get_email})
        # return HttpResponse (json.dumps({
        #     "Email": get_email,
        #     "html": otp1.html}),
        #     content_type="application/json")
        request.session['Email'] = get_email
        # return render_to_response( "otp1.html", {"Email": get_email})
        # return render(request, "otp1.html")
    # return JsonResponse({"Success":success,"Email":get_email})

    return JsonResponse({"Email":get_email, "Success": True})

@csrf_exempt
def otppage(request):
    if request.method == "GET":
        print('OOOOOOOOOOTTTTTTTTTTPPPPPPPP')
        get_email = request.GET.get('Email')
        mymsg =request.GET.get('Message')

        return render(request, "otp1.html",{"Email": get_email,"Message": mymsg})

    elif request.method == "POST":
        myotp = request.POST.get('Otp')
        myemail =request.POST.get('Email')
        print("My Otp========",myotp)
        if Logins.objects.filter(email=myemail).exists():

            print("Inside ifffffffffff")
            data1 = Logins.objects.get(email=myemail)
            print("DDDDDDDDDDDDDDDDDDDAAAAATTTTAAAAAA111111",data1)
            data2 =New.objects.get(new=data1)
            dbotp =data2.otp
            print("MMMMMMMMMYYYYYYYYYYYOOOOTTTTTTPPPPPP",dbotp)
            print("MMMMMMMMMYYYYYYYYYYYOOOOTTTTTTPPPPPP",int(myotp))
            if int(myotp)==dbotp:
                print("Inside Trrrrrrrrrrrruuuuuuuueeeeeeeeeeee")
                return JsonResponse({"Message": "success", "Success": True})
            else:
                print("Inside Fallllllssssssseeeeeee")
                msg = "Please enter correct otp"
                return JsonResponse({"Message": msg, "Success": False})




@csrf_exempt
def home(request):
    if request.method == "GET":
        # print('OOOOOOOOOOTTTTTTTTTTPPPPPPPP')
         print("Insideeeeeeeeeee HOOOOOOOOMEEEEEE")

         return render(request, "home1.html")


@csrf_exempt
def login_login(request):
    return render(request, "Login.html")


@csrf_exempt
def auth(request):
    if request.method == "POST":
        data = Logins.objects.all()
        for i in data:
            email = (i.email)
            pssword = (i.password)
            user = (i.username)
            # decoded = jwt.decode(pssword, 'secret', algorithms='HS256')
            #  email=(i.email)
            no = (i.contactno)
        # user= data.username
        # pssword =data.password
        # email=data.email
        get_email = request.POST.get('Email')
        get_pswd = request.POST.get('Password')
        # get_number=request.POST.get(no)
        if email == get_email and pssword == get_pswd:
            print("true")
            return render(request, "home1.html", {"Username": user, "Email": email,
                                                  "Contact_no": no})
        else:
            msg = "Please enter Correct Details"
            return render(request, "Login1.html", {"Message": msg})
