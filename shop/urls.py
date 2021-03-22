from django.contrib import admin
from django.urls import path
from shop.class_views import LoginView,SignupView,IndexView,sendOtp,verifyCode,productDetails,logout,DownloadFreeView,CreatePaymentView,verifyPayment,downloadPaidProduct,my_orders,ResetPassword,PasswordResetVerification,verifyResetPasswordCode
from . import views
from shop.middleware.login_required_middleware import login_required 
from shop.middleware.can_not_access_after_login import cantaccessafterlogin 

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('login',cantaccessafterlogin(LoginView.as_view()),name="login"),
    path('logout',logout,name="login"),
    path('orders',login_required(my_orders),name="orders"),
    path('signup',cantaccessafterlogin(SignupView.as_view()),name="signup"),
    path('send-otp',sendOtp,name="sendOtp"),
    path('verify',verifyCode,name="verify"),
    path('product/<int:product_id>',productDetails,name="details"),
    path('download-free/<int:product_id>',DownloadFreeView.as_view(),name="downloadfree"),
    path('create-payment/<int:product_id>',login_required(CreatePaymentView.as_view()),name="createpayment"),
    path('complete-payment',login_required(verifyPayment),name="verifypayment"),
    path('download/paidproduct/<int:product_id>',downloadPaidProduct,name="downloadPaidProduct"),
    path('reset-password',ResetPassword.as_view(),name="resetpassword"),
    path('reset-password-verification',PasswordResetVerification.as_view(),name="reset-password-verification"),
    path('verify-reset-password-code',verifyResetPasswordCode,name="verify-reset-password-code"),

]