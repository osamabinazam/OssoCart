from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class AccountManager (BaseUserManager):
    
    # Validating email and username
    def create_user(self,first_name, last_name, username,  email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username') 
        
        user = self.model(
            first_name  =first_name,
            last_name   =last_name,
            username    =username,
            email       =self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)       # Creating user into database
        return user
        
    def create_superuser(self, first_name, last_name, username, email, password):
        
        # Calling to create_user method
        user = self.create_user(
            first_name, 
            last_name, 
            username, 
            email, 
            password,
        )
        
        user.is_staff       = True
        user.is_superuser   = True
        user.is_admin       = True
        user.is_active      = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    email           = models.EmailField(unique=True)
    username        = models.CharField(max_length=50, unique=True)
    phone_number    = models.CharField(max_length=50)
    
    
    # Required Field
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_active       = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)
    
    # Optional Field
    
    # avatar          = models.ImageField(upload_to='avatar', blank=True, null=True)
    # bio             = models.TextField(blank=True, null=True)
    
    # Setting email address as  login method
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'password']
    
    objects = AccountManager()
    
    # String Representation of the model. Email is the String
    def __str__(self):
        return self.email
    
    # Permission to users
    def has_perm(self, prem , obj=None):
        return self.is_admin
    
    # Always true
    def has_module_perms(self, add_label):
        return True