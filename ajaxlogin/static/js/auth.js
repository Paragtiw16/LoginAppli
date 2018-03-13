function click4() {


    var get_email = document.getElementById('email').value;
     var get_pwd = document.getElementById('pwd').value;

    alert(get_email);
    alert(get_pwd);

    $.ajax({
        url: '/auth/',
        type: "POST",
        data: {"Password": get_pwd, "Email": get_email},
        dataType: 'application/json; charset=utf-8',
        success: {}
    });
}