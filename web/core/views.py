from django.shortcuts import render
from django.http import HttpResponse
from .models import Registrationform ,Usertable
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm ,UserDetails
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name', '')
        last_name= request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        mobile_no=request.POST.get('mobile_no', '')
        password = request.POST.get('password', '')
        con_password=request.POST.get('con_password', '')
        registers = Registrationform(first_name=first_name, last_name=last_name, email=email, password=password, con_password=con_password,mobile_no=mobile_no )
        registers.save()
    return render(request, 'core/register.html')


def login(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        password=request.POST['password']
        try:
            user=auth.authenticate(first_name=first_name,password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,'core/index.hml')
            else:
                messages.error(request,'name and password did not matched')   

        except auth.ObjectNotExist:
            print("invalid user")      
    return render (request,'core/login.html')           



def index(request):
    return render(request,'core/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'core/registration.html',
                          {'user_form':user_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'core/log.html', {})                       
#def user_login(request):
 #   if request.method == 'POST':
       # username = request.POST.get('username')
       # password = request.POST.get('password')
        #user = authenticate(username=username, password=password)
       # if user:
           # if user.is_active:
               # login(request,user)
              #  return HttpResponseRedirect(reverse('index'))
           # else:
              #  return HttpResponse("Your account was inactive.")
       # else:
           # print("Someone tried to login and failed.")
          #  print("They used username: {} and password: {}".format(username,password))
           # return HttpResponse("Invalid login details given")
   # else:
       # return render(request, 'core/login.html', {})


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserDetails(data=request.POST)
        if user_form.is_valid():
            df = user_form.save()
            df.set_password(df.password)
            df.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserDetails()
    return render(request,'core/signup.html',
                          {'user_form':user_form,
                           'registered':registered})