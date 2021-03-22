from django.shortcuts import render, HttpResponse,redirect
from shop.models import Product, ProductImages, User,Payment
from shop.utils.email_sender import sendEmail
import random
import math
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.contrib import messages
from django.db.models import Q


def my_orders(request):
    user_id=request.session.get('user').get('id')
    user=User(id=user_id)
    payments=Payment.objects.filter(~Q(status="Failed"),user=user)
    return render(request,"orders.html",{"orders":payments})
    