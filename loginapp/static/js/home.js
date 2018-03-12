function click3()
{
   var name = document.getElementById('uname').value;

   var pwd = document.getElementById('pwd').value;
   var email=document.getElementById('email').value;
   var number=document.getElementById('number').value
   alert(name);
   alert(pwd);
   alert(email);
    alert(number);

    $.ajax({
        url: '/login_login/',
        type: "POST",
        data: {"name":name,"password":pwd,"Email":email,"no":number},
        // dataType: 'application/json; charset=utf-8',
        // success:{}
    });