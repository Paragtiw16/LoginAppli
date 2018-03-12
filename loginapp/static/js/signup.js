function click1()
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
        url: '/otp/',
        type: "POST",
        data: {"name":name,"password":pwd,"Email":email,"no":number},
        // dataType: 'application/json; charset=utf-8',
        // success:{}
    });



    // var i={"name":name};
    // var j={"password":pwd};
    // var k={"Email":email};
    // var l={"no":number};






}