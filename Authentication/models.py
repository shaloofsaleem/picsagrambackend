from django.db import models

from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager):
    def createUser(self, email,password = None, **extra_fields):
        if not email:
            raise ValueError('Please provide an email address')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields): 
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_active') is not True:
            raise ValueError("superuser must be active")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must be staff")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser must be superuser")
        return self.createUser(email, password, **extra_fields)
    
class User(AbstractUser):
    email =models.EmailField(max_length=225,unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=70) 
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    object = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']   
    def get_short_name(self) -> str:
        return self.first_name 
    def __str__(self) -> str:
        return self.email
            

