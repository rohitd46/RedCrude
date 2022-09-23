from django.contrib import admin
from django.urls import path
from Redcrude_App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.INDEX,name='index'),
    path('login',views.LOGIN,name='login'),
    path('signupuser',views.SIGNUPUSER,name='signupuser'),
    path('signupteacher',views.SIGNUPTEACHER,name='signupteacher'),
    path('signuptrader',views.SIGNUPTRADER,name='signuptrader'),
    path('forgetpassword',views.ForgetPassword,name='forgetpassword'),
    path('succes',views.Succes,name='succes'),
    path('error',views.Error,name='error'),
    path('tokensend',views.token_send,name='tokensend'),
    path('verify/<auth_token>',views.verify,name='verify'),
    path('Dashboard',views.USERDASHBOARD,name='Dashboard'),
    path('logout', views.Logout,name='logout'),
]