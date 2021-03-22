from django.shortcuts import render, HttpResponse,redirect
from shop.models import Product, ProductImages, User,Payment
from shop.utils.email_sender import sendEmail
import random
import math
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.contrib import messages


class DownloadFreeView(View):
    def get(self, request,product_id):
        try:
            product=Product.objects.get(id=product_id)
            if product.descount==100:
                return redirect(product.file.url)
            else:
                return redirect('index')
        except:
            return redirect('index')


def downloadPaidProduct(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
        print(product)
        session_user=request.session.get('user')
        user=User(id=session_user.get('id'))
        print(user)
        payment=Payment.objects.filter(user=user,name=product)
        print(payment)
        # messages.success(request,"file downloaded successfully")
        file=product.file
        if file:
            return redirect(product.file.url)
        else:
            return redirect(product.link)
    except:
        messages.error(request,"please payment first then download")
        return redirect('index')


        
        
        




    