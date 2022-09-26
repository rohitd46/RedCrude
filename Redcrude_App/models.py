from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=(
        ('admin','admin'),
        ('teacher','teacher'),
        ('trader','trader'),
        ('user','user'),
    )
    
    user_type=models.CharField(choices=USER, max_length=50,default='admin')
    phonenumber=models.CharField(max_length=10)
    
class Users(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.admin.first_name
    
class Teacher(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.admin.first_name
    
class Trader(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.admin.first_name

class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)