function click1() {
    var name = document.getElementById('uname').value;
    var pwd = document.getElementById('pwd').value;
    var email = document.getElementById('email').value;
    var number = document.getElementById('number').value;
    alert(name);
    $.ajax({
        url: '/ajax/signup/',
        method: 'POST',
        data: {"name": name, "password": pwd, "Email": email, "no": number},
        // dataType: 'application/json; charset=utf-8',
         success:function (text) {
                   alert("Mmmmmmmeeeeessssaaagggeeee");
                   console.log(text);
                    alert(text);
                   if(text.Success==true)
                   {
                       console.log(text.Email);
                       get_email=text.Email;
                       window.location.href="/ajax/otppage?Email="+get_email
                       // "Email":get_email

                   }





         }
    });
}