function click4() {
    var name = document.getElementById('uname').value;
    var email = document.getElementById('email').value;
    var number = document.getElementById('number').value;

    alert(name);

    $.ajax({
        url: '/login_login/',
        type: "POST",
        data: {"User": get_user, "Email": get_email,"Contact_no":get_cno},
        dataType: 'application/json; charset=utf-8',
        success: {}
    });
}