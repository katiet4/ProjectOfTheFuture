function validate_form ( )
{   
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var email = document.contact_form.email.value;
    var password = document.contact_form.password.value;
        if ( email != "" && password != "")
        {
            if(password.length >= 8){
                if(reg.test(email)){
                     document.contact_form.login.style = 'color:green;'; 
                     return true;
                }
               
            }
        }

       document.contact_form.login.style = 'color:red;'; 
       return false
}