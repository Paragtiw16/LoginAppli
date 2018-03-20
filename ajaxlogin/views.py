import json

import jwt
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
        myemail = request.GET.get('Email')
        mymsg =request.GET.get('Message')

        # myemail=request.GET.get('Emaaill')
        if myemail is None:
            print("Inssssiiiiideeeee Faaalllseee case IIIFFFFF")
            femail=request.GET.get('MyEmail')
            print("False caseeeeeee Emmmaaaailllll=====",femail)
            myemail=femail
            print("Assssssssssiiiignnnnnmmmeeennntttttt===",myemail)
        return render(request, "otp1.html",{"Email": myemail,"Message": mymsg})

    elif request.method == "POST":
        myotp = request.POST.get('Otp')
        myemaill =request.POST.get('Email')
        print("My Otp========",myotp)
        if Logins.objects.filter(email=myemaill).exists():

            print("Inside ifffffffffff")
            data1 = Logins.objects.get(email=myemaill)
            print("DDDDDDDDDDDDDDDDDDDAAAAATTTTAAAAAA111111",data1)
            data2 =New.objects.get(new=data1)
            dbotp =data2.otp
            print("MMMMMMMMMYYYYYYYYYYYOOOOTTTTTTPPPPPP",dbotp)
            print("MMMMMMMMMYYYYYYYYYYYOOOOTTTTTTPPPPPP",int(myotp))
            if int(myotp)==dbotp:
                print("Inside Trrrrrrrrrrrruuuuuuuueeeeeeeeeeee")
                del request.session['Email']
                # print("Sesssionn Emmmaaillll=",get_email)
                # request.session['Email'] = get_email
                return JsonResponse({"Message": "success", "Success": True})
            else:
                print("Inside Fallllllssssssseeeeeee")
                msg = "Please enter correct otp"
                print("Fallllseeee Emmmaailllll=====", myemaill)
                return JsonResponse({"Message": msg, "Success": False,"Email":myemaill})


@csrf_exempt
def home(request):
    if request.method == "GET":
        # print('OOOOOOOOOOTTTTTTTTTTPPPPPPPP')
         print("Insideeeeeeeeeee HOOOOOOOOMEEEEEE")
         key = 'secret'
         encoded=request.GET.get('Token')
         print("getting encoding value=",encoded)
         decoded = jwt.decode(encoded, key, algorithms='HS256')
         encoded = jwt.encode(decoded, key, algorithm='HS256')

         print("Decodedddddddd Jsssooonnnn=",decoded)
         ID=decoded['Id']
         print("Idddddd=====",ID)
         try:

             data1 = Logins.objects.get(id=ID)
         except Exception, e:
               print("Apna  Error=", str(e))
         print(data1)
         username=data1.username
         email =data1.email
         contactno=data1.contactno
         encoded = jwt.encode(decoded, key, algorithm='HS256')
         return render(request, "home1.html",{"Email":email,"Username":username,
                                              "Contact_no":contactno,"Encoded":encoded})


@csrf_exempt
def login_login(request):
    print("Checking loginnnn Conditionnnnnn")
    if request.method == "GET":
        print("Innnnnsssiiiiiidddeee Lllllooogggiiinnnn   GGGETTT")
        # mymsg = request.GET.get('Message')
        # print("Alerrrrtttt messageeeee",mymsg)
        return render(request, "Login1.html")

    elif request.method == "POST":
        print("Insiddeeeeee llooooogggiiinnn POOOOSSTTT")
        myemail=request.POST.get('Email')
        mypassword=request.POST.get('Password')
        print("User entered Email=", myemail)
        print("User entered Password=", mypassword)
        flag=Logins.objects.filter(email=(myemail)).exists()
        if flag==True:
                print("Insideee Flaggggggggggggg")

                data1=Logins.objects.get(email=myemail)

                email=data1.email
                print("Database email=", email)
                pssword=data1.password
                print("Database password=", pssword)
                id=data1.id


                if   pssword==mypassword:

                    print("MyEmail==",myemail)
                    key = 'secret'
                    encoded=jwt.encode({'email':myemail,'Id':id},key,algorithm='HS256')
                    # request.session['Encoded'] =encoded
                    print("afterrr ennncoooddingggg")
                    return JsonResponse({"Message": "success", "Success": True,
                                         "Encoded":encoded})
                else:
                    print("Inside else incorrect detailssss")
                    msg="Please enter correct Details"
                    print("Messaaggeeeeee=",msg)
                    return JsonResponse({"Message": msg, "Success": False})

        else:
            print("Inside else incorrect detailssss")
            msg = "Please enter correct Details"
            print("Messaaggeeeeee=", msg)
            return JsonResponse({"Message": msg, "Success": False})





@csrf_exempt
def edit(request):
    if request.method == "GET":
        print("Inside Ediiitttttt GETTTT")
        encoded = request.GET.get('Token')

        key = 'secret'
        decoded = jwt.decode(encoded, key, algorithms='HS256')
        print("Decodedddddddd Jsssooonnnn inside Edit get=", decoded)
        ID = decoded['Id']
        print("Idddddd=====", ID)
        try:

            data1 = Logins.objects.get(id=ID)
        except Exception, e:
            print("Apna  Error=", str(e))
        print(data1)
        username = data1.username
        contactno = data1.contactno
        encoded = jwt.encode(decoded, key, algorithm='HS256')
        print("Enddd off Edittt GEEETTTTTT")
        return JsonResponse ({"Username": username,"Contact_no": contactno,
                              "Encoded": encoded,"Message": "success", "Success": True})

    elif request.method == "POST":
        print("inside signup POST Method")
        get_user = request.POST.get('User')
        get_contact = request.POST.get('Contact')
        get_email = request.POST.get('Email')
        token = request.POST.get('Encoded')
        print("get_uname ", get_user)
        print("get_email ", get_email)
        key = 'secret'
        decoded = jwt.decode(token, key, algorithms='HS256')
        print("Decodedddddddd Jsssooonnnn=", decoded)
        ID = decoded['Id']
        print("Idddddd=====", ID)
        try:

            data1 = Logins.objects.get(id=ID)
        except Exception, e:
            print("Apna  Error=", str(e))
        print(data1)
        data1.username=get_user
        data1.email=get_email
        data1.contactno=get_contact
        data1.save()
        msg = "Data has been saved"
        print("Messaaggeeeeee=", msg)
        encoded = jwt.encode(decoded, key, algorithm='HS256')
        return JsonResponse({"Message": "success", "Success": True,"Message": msg,
                             "Token": encoded})