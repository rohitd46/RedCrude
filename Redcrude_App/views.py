from email import message
from unicodedata import name
from django.shortcuts import render,redirect,HttpResponse
from Redcrude_App.emailbackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from Redcrude_App.models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def INDEX(request):
    return render(request,'index.html')

def LOGIN(request):
    if request.method=='POST':
        user=EmailBackend.authenticate(request,username=request.POST.get('email'),
                                       password=request.POST.get('password'))
        
        # profile_obj=Profile.objects.filter(user=user).first()
        # if not profile_obj.is_verified:
        #     return redirect('login')
        if user!= None:
            login(request,user)
            user_type=user.user_type
            if user_type=='admin':
                return redirect ("Dashboard")
            elif user_type=='teacher':
                 return redirect ("Dashboard")
            elif user_type=='trader':
                 return redirect ("Dashboard")
            elif user_type=='user':
                 return redirect ("Dashboard")
            else:
                return redirect('login')
        else:
            return redirect('login')
    return render(request,'login.html')

def SIGNUPUSER(request):
      if request.method=="POST":
          first_name=request.POST.get('first_name')  
          phonenumber=request.POST.get('phonenumber')  
          email=request.POST.get('email')  
          password=request.POST.get('password')  
          
          if CustomUser.objects.filter(email=email).exists():
              return redirect('signupuser')
          else:
              user=CustomUser(first_name=first_name,username=first_name,email=email,user_type='user')
              user.set_password(password)
              user.save()
              us=Users(admin=user,phonenumber=phonenumber)
              us.save()
            #   auth_token=str(uuid.uuid4())
            #   profile_obj=Profile.objects.create(user=user,auth_token=auth_token)
            #   profile_obj.save()
            #   verify_send_email(email,auth_token)
              return redirect('login')
          
      return render(request,'signupuser.html')

def SIGNUPTEACHER(request):
    if request.method=="POST":
          first_name=request.POST.get('first_name')  
          phonenumber=request.POST.get('phonenumber')  
          email=request.POST.get('email')  
          password=request.POST.get('password')  
          
          if CustomUser.objects.filter(email=email).exists():
              return redirect('signupuser')
          else:
              user=CustomUser(first_name=first_name,username=first_name,email=email,user_type='teacher')
              user.set_password(password)
              user.save()
              techer=Teacher(admin=user,phonenumber=phonenumber)
              techer.save()
            #   auth_token=str(uuid.uuid4())
            #   profile_obj=Profile.objects.create(user=user,auth_token=auth_token)
            #   profile_obj.save()
            #   verify_send_email(email,auth_token)
              return redirect('login')
    return render(request,'signupteacher.html')

def SIGNUPTRADER(request):
    if request.method=="POST":
          first_name=request.POST.get('first_name')  
          phonenumber=request.POST.get('phonenumber')  
          email=request.POST.get('email')  
          password=request.POST.get('password')  
          
          if CustomUser.objects.filter(email=email).exists():
              return redirect('signupuser')
          else:
              user=CustomUser(first_name=first_name,username=first_name,email=email,user_type='trader')
              user.set_password(password)
              user.save()
              trader=Trader(admin=user,phonenumber=phonenumber)
              trader.save()
            #   auth_token=str(uuid.uuid4())
            #   profile_obj=Profile.objects.create(user=user,auth_token=auth_token)
            #   profile_obj.save()
            #   verify_send_email(email,auth_token)
              return redirect('login')
    return render(request,'signuptrader.html')

def ForgetPassword(request):
    return render(request,'forgetpassword.html')

# def Succes(request):
#     return render(request,'succes.html')

# def token_send(request):
#     return render(request,'tokensend.html')


# def Error(request):
#     return render(request,'error.html')


# def verify(request,auth_token):
#     profile_obj=Profile.objects.filter(auth_token=auth_token).first()
#     if profile_obj:
#         profile_obj.is_verified=True
#         profile_obj.save()
#         return redirect('succes')
#     else:
#         return redirect('error')

# def verify_send_email(email,token):
#     subject="Your Account need to be Verifiy"
#     message=f"Click this link to verify your account http://127.0.0.1:8000/verify/{token}"
#     email_form=settings.EMAIL_HOST_USER
#     recipient_list=[email]
#     send_mail(subject,message,email_form,recipient_list)

@login_required(login_url='login')    
def USERDASHBOARD(request):
    return render (request,'userindex.html')

def Logout(request):
    logout(request)
    return redirect('login')

def About(request):
    return render(request,'about.html')

def AllCrepto(request):
    return render(request,'allcrpto.html')

def Market(request):
    return render(request,'market.html')

def Pricing(request):
    return render(request,'pricing.html')

def Term(request):
    return render(request,'trmcon.html')

def Freatue(request):
    return render(request,'freatue.html')

def Privacy(request):
    return render(request,'privacy.html')

def Contect(request):
    return render(request,'contect.html')

def Blog(request):
    return render(request,'blog.html')