from django import forms
from .models import UserProfileInfo , Usertable
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    mobile_no=forms.CharField(max_length=10)
    state=forms.CharField(max_length=50)
    pincode=forms.CharField(max_length=50)


    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')


class UserDetails(forms.ModelForm):
    mobile_no=forms.CharField(max_length=10)


    class Meta():
        model=User
        fields = ('email','first_name','last_name','username')

        
