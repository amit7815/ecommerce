from django.shortcuts import render,redirect
from django.contrib import messages
def cantaccessafterlogin(get_response):
    def middleware(request):
        print("middleware.....")
        user=request.session.get('user')
       
        if user:
            #dont serve page
            messages.error(request,"You are already login")
            return redirect("index")
        else:
            return get_response(request)


    return middleware