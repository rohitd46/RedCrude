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
    # path('succes',views.Succes,name='succes'),
    # path('error',views.Error,name='error'),
    # path('tokensend',views.token_send,name='tokensend'),
    # path('verify/<auth_token>',views.verify,name='verify'),
    path('Dashboard',views.USERDASHBOARD,name='Dashboard'),
    path('logout', views.Logout,name='logout'),
    path('about', views.About,name='about'),
    path('allcreptacurrncy', views.AllCrepto,name='allcrepto'),
    path('market', views.Market,name='market'),
    path('pricing', views.Pricing,name='pricing'),
    path('terms-conditions', views.Term,name='terms-conditions'),
    path('privacy-policy', views.Privacy,name='privacy-policy'),
    path('freatue-business', views.Freatue,name='freatue-business'),
    path('contect', views.Contect,name='contect'),
    path('blog', views.Blog,name='blog'),
]