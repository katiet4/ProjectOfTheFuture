function validate_form ( )
{   
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var email = document.contact_form.index_email.value;
    var NickName = document.contact_form.NickName.value;
    var index_pass = document.contact_form.index_pass.value;
    var FirstName = document.contact_form.FirstName.value;
    var LastName = document.contact_form.LastName.value;
    var radio = document.contact_form.radio.value;
    var day = document.contact_form.day.value;
    var month = document.contact_form.month.value;
    var year = document.contact_form.year.value;
        if ( email != "" && NickName != "" && index_pass != ""
         && FirstName != "" && LastName != "" && radio != ""
         && day != 0 && month != 0 && year != 0)
        {
            if(index_pass.length >= 8){
                if(reg.test(email)){
                     document.contact_form.postLogin.style = 'color:green;'; 
                     return true;
                }
               
            }
        }

       document.contact_form.postLogin.style = 'color:red;'; 
       return false
}