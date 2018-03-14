function click2() {
    var otp = document.getElementById('otp').value;

    var get_email = document.getElementById('email').value;

    alert(otp);
    alert(get_email);

    $.ajax({
        url: '/ajax/home/',
        type: "POST",
        data: {"Otp": otp, "Email": get_email},
        dataType: 'application/json; charset=utf-8',
        success: {}
    });
}