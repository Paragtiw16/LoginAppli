function click2() {
    var get_otp = document.getElementById('otp').value;
    var myemail  = document.getElementById('emmail').value;

    alert(get_otp);
    console.log(myemail);
    // alert(myemail);

    $.ajax({

        url: '/ajax/otppage/',
        method: "POST",
        // data: {"Otp": otp, "Email": get_email},
        data:{"Otp":get_otp,"Email":myemail},

        // dataType: 'application/json; charset=utf-8',
        success:function (script)
        {
            alert("HHHHHHHHEEEEEEEELLLLLLLLOOOOOOOOO");
            console.log(script);
                    alert(script);
                    alert(script.Success);
             if(script.Success==true)
                   {
                       console.log("Insideee successsss off successs of otp");
                       window.location.href="/ajax/login_login";
                   }
             else
                    {
                        console.log("Innnnsiiiideee Faaalllseee");
                        console.log(script.Message);
                        get_msg=script.Message;
                        console.log(script.Email);
                        myemaill=script.Email;
                        console.log(myemaill);
                        window.location.href="/ajax/otppage?Message="+get_msg+"&MyEmail="+myemaill




                        
                      }

        }
    });
}