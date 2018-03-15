function click2() {
    var get_otp = document.getElementById('otp').value;

    // var get_email = document.getElementById('email').value;

    alert(get_otp);
    // alert(get_email);

    $.ajax({

        url: '/ajax/otppage/',
        method: "POST",
        // data: {"Otp": otp, "Email": get_email},
        data:{"Otp":get_otp},

        // dataType: 'application/json; charset=utf-8',
        success:function (script)
        {
            alert("HHHHHHHHEEEEEEEELLLLLLLLOOOOOOOOO");
            console.log(script)
                    alert(script)
             if(script.Success==true)
                   {
                       window.location.href="/ajax/home"
                   }
             else (script.Success==False)
                    {
                        window.location.href="/ajax/otppage"
                        
                      }

        }
    });
}