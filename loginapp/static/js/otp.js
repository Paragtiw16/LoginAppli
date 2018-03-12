function click2() {
    var otp = document.getElementById('otp').value;
    // {{ Email }}
    var get_email = document.getElementById('email').value;
    // var pwd = document.getElementById('pwd').value;
    // var email=document.getElementById('email').value;
    // var number=document.getElementById('number').value
    // alert(name);
    // alert(pwd);
    // alert(email)
    alert(otp)
    alert(get_email)

    $.ajax({
        url: '/home/',
        type: "POST",
        data: {"otp": otp, "Email": get_email},
        dataType: 'application/json; charset=utf-8',
        success: {}
    });
}