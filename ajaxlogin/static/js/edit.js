function click4() {
    var get_token = document.getElementById('token').value;
    // var get_user = document.getElementById('user').value;
    // var get_email = document.getElementById('email').value;
    // var get_cno = document.getElementById('cno').value;
    // var encoded = document.getElementById('Encoded').value;


    alert(get_token);

    $.ajax({
        url: '/ajax/edit/',
        type: "GET",
        data: {"Token":get_token},
        // dataType: 'application/json; charset=utf-8',
         success:function (profile) {
                    alert("Insideeee Successss EDIIT GETTT");
                    alert("Profileeeeeeeeeeeeee")
                    console.log(profile);

             if(profile.Success==true)
                   {
                       console.log(profile.Username);
                       console.log(profile.Contact_no)
                       myuser=profile.Username;
                       contactn=profile.Contact_no;
                       encoded=profile.Encoded;
                       document.getElementById('user').value=myuser
                       document.getElementById('cno').value=contactn
                       $('#div_tag').show();

                   }
             // else
             //        {
             //            console.log("Innnnsiiiideee Faaalllseee of login  jssss");
             //            console.log(check.Message);
             //            alert(check.Message);
             //
             //            window.location.href="/ajax/login_login";
             //
             //
             //
             //          }
        }
    });
}