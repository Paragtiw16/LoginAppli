function click5() {
    var get_user = document.getElementById('user').value;
    var get_email = document.getElementById('email').value;
    var get_cno = document.getElementById('cno').value;
    var encoded = document.getElementById('Encoded').value;

    alert(get_email);
    alert(get_user);

    $.ajax({

        url: '/ajax/edit/',
        method: "POST",
        data: {"Email": get_email,"User":get_user,"Contact":get_cno,"Encoded":encoded},
        // dataType: 'application/json; charset=utf-8',
        success:function (field) {
                    console.log(field);
                    alert(field);
                    alert(field.Success);


             if(field.Success==true)
                   {

                       console.log("Insideeeee succcessss offf LLLooogginnn");
                       token=field.Token
                       alert(field.Message)
                       window.location.href="/ajax/home?Token="+token;
                   }





        }
    });
}