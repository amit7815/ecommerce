from django.shortcuts import render, HttpResponse,redirect
from shop.models import Product, ProductImages, User,Payment
from shop.utils.email_sender import sendEmail
import random
import math
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from django.contrib import messages
from instamojo_wrapper import Instamojo
from fullecomm.settings import PAYMENT_API_AUTH_TOKEN,PAYMENT_API_KEY 
from django.contrib import messages

API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')


def verifyPayment(request):
    payment_id=request.GET.get('payment_id')
    payment_request_id=request.GET.get('payment_request_id')
    print(payment_id, payment_request_id)
    user=request.session.get('user')
    print(user)
    userObject=User.objects.get(id=user.get('id'))
    response = API.payment_request_payment_status(payment_request_id, payment_id)

    print(response)
    status=response['payment_request']['payment']['status']
    # import json
    # return HttpResponse(json.dumps(response))
    if status is not "Failed":
        payment=Payment.objects.get(payment_request_id=payment_request_id)
        payment.payment_id=response['payment_request']['payment']['payment_id']
        payment.status=status
        payment.save()
        print(f"payment status is {payment.status} ,status is {status}")
        return render(request,"download_product_after_payment.html",{'payment':payment})
    else:
        messages.error(request,"something is wrong")
        return redirect("index")

    print(payment_id,payment_request_id)
    

class CreatePaymentView(View):
    def get(self, request,product_id):
        user=request.session.get('user')
        product=Product.objects.get(id=product_id)
        userObject=User.objects.get(id=user.get('id'))
        amount=product.price-(product.price*(product.descount/100))
        response = API.payment_request_create(
            amount=math.floor(amount),
            purpose=f'Payment for {product.name}',
            send_email=True,
            phone=userObject.phone,
            buyer_name=userObject.name,
            email=user.get('email'),
            redirect_url="http://localhost:8000/complete-payment"
        )
    # print the long URL of the payment request.
        
        payment_request_id=response['payment_request']['id']
        payment=Payment(user=User(id=user.get('id')),name=Product(id=product_id),payment_request_id=payment_request_id)
        payment.save()
        url=response['payment_request']['longurl']
    # print the unique ID(or payment request ID)
        print(response)
        return redirect(url)


    