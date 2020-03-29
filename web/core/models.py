from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registrationform(models.Model):
    email=models.EmailField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=10)
    password=models.CharField(max_length=30) 
    con_password=models.CharField(max_length=30,default='')

    def __str__(self):
        return self.first_name 


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_no=models.CharField(max_length=10)
    state=models.CharField(max_length=50,default='')
    pincode=models.CharField(max_length=10,default='')
    def __str__(self):
        return self.user.username


class Usertable(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_no=models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name