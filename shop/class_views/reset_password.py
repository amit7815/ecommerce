from django.views import View
from django.contrib.auth.hashers import check_password,make_password
from shop.models import User
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from shop.utils.email_sender import sendEmail
import math
import random


class ResetPassword(View):
    def get(self, request):
        return render(request,"reset_password.html",{"step1":True})

    def post(self,request):
        password=request.POST.get('password')
        repassword=request.POST.get('cpassword')
        error=None
        if len(password)<6:
            error="password must be more than 6 character"
        elif len(repassword)<6:
            error="Confirm password must be more than 6 character"
        elif password!=repassword:
            error="password not match re-enter passwords"
        if error:
            return render(request,"reset_password.html",{'step3':True,"error":error})
        else:
            email=request.session.get('reset-password-email')
            user=User.objects.get(email=email)
            user.password=make_password(password)
            user.save()
            request.session.clear()
            sendEmailAfterChangePassword(user)
            messages.success(request,"Password Changed SuccessFully ! Login Now")
            return render(request,"login.html")

def sendEmailAfterChangePassword(user):
    html="<h2>Password Changed Successfully.......<h2>"
    sendEmail(user.name,user.email,"Password Changed",html)

        
        

    


class PasswordResetVerification(View):
    def post(self, request):
        print(request.POST.get('email'))
        email=request.POST.get('email')
        user=User.objects.get(email=email)
        try:
            otp=math.floor(random.random()*1000000)
            html=f'''
                <h4>Your Password verification code is  {otp}</h4>
        
                '''
            sendEmail("User",
                    email,
                    "Password reset verification code",html)
            request.session['reset-password-verification-code']=otp
            request.session['reset-password-email']=email
            messages.success(request,"verification code is sent successfully check your email")
            return render(request,"reset_password.html",{"step2":True})
        except:
            messages.error(request,"email not registered")
            return redirect("/reset-password")


def verifyResetPasswordCode(request):
    code=request.POST.get('code')
    sessioncode=request.session['reset-password-verification-code']
    print(code)
    print(sessioncode)
    if code==str(sessioncode):
        messages.success(request,"verification code is matched Change Your password now")
        return render(request,"reset_password.html",{"step3":True})
    else:
        messages.error(request,"verification code is not matched")
        return render(request,"reset_password.html",{"step2":True})
       