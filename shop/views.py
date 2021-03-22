from django.shortcuts import render, HttpResponse,redirect
from .models import Product, ProductImages, User
from .utils.email_sender import sendEmail
import random
import math
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.


# def index(request):

#     products = Product.objects.filter(active=True)
#     print(products)
#     context = {
#         'products': products
#     }
#     return render(request, 'index.html', context)


# def login(request):
#     if request.method=='GET':
#         return render(request, 'login.html')
#     email=request.POST.get('email')
#     password=request.POST.get('password')
#     try:
#         user=User.objects.get(email=email)
#         flag=check_password(password=password,encoded=user.password)
#         if flag:
#             return redirect('index')
#         else:
#             return render(request, 'login.html',{'error':"email or password is invalid "})
        
#     except:
#         return render(request, 'login.html',{'error':"email or password is invalid "})


# def signup(request):
#     if request.method == 'POST':
#         try:

#            # print(request.POST)
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             phone = request.POST.get('phone')
#             hashedpassword=make_password(password)
#             user = User(name=name, email=email, password=hashedpassword, phone=phone)
#             user.save()
#             return render(request, 'login.html')
#         except:
#              return render(request,'signup.html',{'error':"User already registered...."})
           
#     return render(request,'signup.html')

def productDetails(request,product_id):
    product=Product.objects.filter(id=product_id)
    images=ProductImages.objects.filter(product=product_id)
    return render(request,'product_detail.html',{'product':product[0],'images':images})

# def sendOtp(request):
#     name=request.POST.get('name')
#     email=request.POST.get('email')
#     otp=math.floor(random.random()*1000000)
#     html=f'''
#         <p>Hello <b>{name} </b></p>
#         <p>Your Verification code is <b>{otp}</b></p>
#         <p>If you don't requested to this email .you can ignore this email.</p>
# '''
#     if name and email:
#         response=sendEmail(email=email,htmlcontent=html,name=name,subject='Verify Email')


#     # email sending 

#         try:
#             if response:
#                 request.session['verification-code']=otp
#                 return HttpResponse("{'message':'success'}",status=200)
#             else:
#                 return HttpResponse(status=400)
#         except:
#             return HttpResponse(status=400 )


# def verifyCode(request):
#     code=request.POST.get('code') #str
#     otp=request.session.get('verification-code')   #integer
#     print(code,otp)
#     if code==str(otp):
#         return HttpResponse("{'message':'success'}",status=200)
#     else:
#         return HttpResponse(status=400)

