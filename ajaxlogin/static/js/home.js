function click4() {
    var get_email = document.getElementById('email').value;

    var get_user = document.getElementById('user').value;

     var get_cno = document.getElementById('cno').value;


    alert(otp);
    alert(get_email);

    $.ajax({
        url: '/login_login/',
        type: "POST",
        data: {"User": get_user, "Email": get_email,"Contact_no":get_cno},
        dataType: 'application/json; charset=utf-8',
        success: {}
    });
}