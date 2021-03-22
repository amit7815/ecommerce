from django.shortcuts import render, HttpResponse,redirect
from shop.models import Product, ProductImages, User,Payment
from shop.utils.email_sender import sendEmail
import random
import math
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.db.models import Q

def productDetails(request,product_id):
    product=Product.objects.get(id=product_id)
    print(product)
    images=ProductImages.objects.filter(product=product_id)
    can_download=None
    try:
        session_user=request.session.get('user')
        print(session_user)
        if session_user:
            user_id=session_user.get('id')

            print(user_id)
            user=User.objects.get(id=user_id)
            print(user)
            payment=Payment.objects.filter(~Q(status="Failed"),user=user,name=product)
            print(payment)
            if len(payment)!=0:
                can_download=True
    except:
        pass
    return render(request,'product_detail.html',{'product':product,'images':images,'can_download':can_download})