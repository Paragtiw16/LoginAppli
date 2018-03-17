function click3() {


    var get_email = document.getElementById('email').value;
    var get_pwd = document.getElementById('pwd').value;

    alert(get_email);
    alert(get_pwd);

    $.ajax({

        url: '/ajax/login_login/',
        method: "POST",
        data: {"Password": get_pwd, "Email": get_email},
        // dataType: 'application/json; charset=utf-8',
        success:function (check) {
                    console.log(check);
                    alert(check);
                    alert(check.Success);
             if(check.Success==true)
                   {
                       console.log("Insideeeee succcessss offf LLLooogginnn");
                       window.location.href="/ajax/home";
                   }
             else
                    {
                        console.log("Innnnsiiiideee Faaalllseee of login  jssss");
                        console.log(check.Message);
                        get_msg=check.Message;
                        alert(get_msg)
                        window.location.href="/ajax/login_login";



                      }
        }
    });
}