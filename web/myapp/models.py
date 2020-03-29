from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    dob=models.DateTimeField()

    def __str__(self):
        return self.name


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

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class SavedEmbeds(models.Model):
    type = models.CharField(max_length=15)
    provider_url = models.URLField()
    provider_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    html = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    author_url = models.URLField()
    author_name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title        
 