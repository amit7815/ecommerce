var token=null
// var loading=null;

// window.onload=function(){
//     console.log("onload");
//     loading=document.getElementById('load');
//     loading.hidden=false;
// }

function validate(event){
    // var loading=document.getElementById('load');
    // loading.hidden=false
    var error=document.getElementById('message');
    // error.hidden=false
    var message =null;
    var form =event.target;
    var values=form.elements;
    message=validateForm(form);
    token=values.csrfmiddlewaretoken.value;
    

    
    

    if(message){
        error.innerHTML=message;
        error.hidden=false;
    }
    else{
        error.innerHTML="";
        error.hidden=true;
        var name=values.name.value;
        var email=values.email.value;
        try{
            sendEmail(email,name,token);
        }catch(err){
            console.log(err);
        }
    }

    // alert("amit");
    event.stopPropagation();
    return false;
}


function validateForm(form){
    var values=form.elements;
    token=values.csrfmiddlewaretoken.value;
    var message=null;
    var name=values.name.value;
    var email=values.email.value;
    var password=values.password.value;
    var repassword=values.repassword.value;
    var phone=values.phone.value;

    if(!name.trim()){
        message="name is required";
    }else if(!email.trim()){
        message="email is required";
    }else if(!password.trim()){
        message="enter your password";
    }else if(!repassword.trim()){
        message="enter password again";
    }else if(password.trim()!=repassword.trim()){
        message="password not matched";
    }
    return message
}

function sendEmail(email, name,token){
    var loading=document.getElementById('load')
    loading.hidden=false;
    $.ajax({
        method: "POST",
        url: "/send-otp",
        data: { name: name, email: email ,'csrfmiddlewaretoken':token}
      })
        .done(function( msg ) {
        //   alert( "Code Verified: " + msg );
            loading.hidden=true;
            showOtpInput();
        }).fail(function(err){
            loading.hidden=true;
            alert("can't send email")
        })
        ;
}

function showOtpInput(){
    var otpInput=document.getElementById('verificationInput');
    var verify=document.getElementById('verifyButton');
    var submit=document.getElementById('submitButton');
    otpInput.hidden=false
    submit.hidden=true
    verify.hidden=false
}

function verifyCode(){
    var codeInput=document.getElementById("code");
    var code=codeInput.value;
    var loading=document.getElementById('load')
    loading.hidden=false;
    $.ajax({
        method: "POST",
        url: "/verify",
        data: { 'code': code,'csrfmiddlewaretoken':token}
      })
        .done(function( msg ) {
        //   alert( "Code verified: " + msg );
        loading.hidden=true;
        alert('submit form1')
          submitForm();
            // showOtpInput();
        }).fail(function(err){
            loading.hidden=true;
            alert("code is invalid")
        })
        ;
}

function submitForm(){
    alert("submit form")
    form=document.getElementById('form');
    var message=validateForm(form);
    if(message){}
    else{
        form.submit();
    }
    alert("form submitted")
    // form.submit();
    
}