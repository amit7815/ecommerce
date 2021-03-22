from django.views import View
from django.contrib.auth.hashers import check_password,make_password
from shop.models import User
from django.shortcuts import render,redirect
from django.contrib import messages

class SignupView(View):
    def get(self, request):
        return render(request,'signup.html')

    def post(self, request):
        print(request.POST)
        try:

           # print(request.POST)
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            hashedpassword=make_password(password)
            user = User(name=name, email=email, password=hashedpassword, phone=phone)
            user.save()
            print(user)
            messages.success(request,"Your acccount created successfully login now")
            return render(request, 'login.html')
        except:
            messages.error(request,"User already registered please login ")
            return render(request,'signup.html')
