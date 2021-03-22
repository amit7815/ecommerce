from django.views import View
from django.contrib.auth.hashers import check_password
from shop.models import User
from django.shortcuts import render,redirect
from django.contrib import messages


class LoginView(View):
    return_url=None
    def get(self, request):
        LoginView.return_url=request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            print(user.name)
            flag = check_password(password=password, encoded=user.password)
            if flag:
                temp={}
                temp['email']=user.email;
                temp['id']=user.id;
                temp['name']=user.name;
                request.session['user']=temp;
                messages.success(request,"Successfully Logged in")
                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': "email or password is invalid "})

        except:
            return render(request, 'login.html', {'error': "email or password is invalid "})
