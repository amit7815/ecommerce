from django.shortcuts import render, HttpResponse,redirect
from shop.models import Product, ProductImages, User
from shop.utils.email_sender import sendEmail
import random
import math
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.contrib import messages


def sendOtp(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    otp=math.floor(random.random()*1000000)
    html=f'''
        <p>Hello <b>{name} </b></p>
        <p>Your Verification code is <b>{otp}</b></p>
        <p>If you don't requested to this email .you can ignore this email.</p>
'''
    if name and email:
        response=sendEmail(email=email,htmlcontent=html,name=name,subject='Verify Email')


    # email sending 

        try:
            if response:
                request.session['verification-code']=otp
                return HttpResponse("{'message':'success'}",status=200)
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400 )


def verifyCode(request):
    code=request.POST.get('code') #str
    otp=request.session.get('verification-code')   #integer
    print(code,otp)
    if code==str(otp):
        return HttpResponse("{'message':'success'}",status=200)
    else:
        return HttpResponse(status=400)


    