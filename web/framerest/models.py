from django.db import models

# Create your models here.

class Registration(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    pincode=models.CharField(max_length=35)


    def __str__(self):
        return self.username


class Registrationform(models.Model):
    email=models.EmailField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=10)
    password=models.CharField(max_length=30) 
    con_password=models.CharField(max_length=30,default='')

    def __str__(self):
        return self.first_name       