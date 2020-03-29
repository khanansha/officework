from django.shortcuts import render
from .models import Registration,Registrationform
from django.http import HttpResponse
from django.conf import settings
import requests
from .forms import SubmitEmbed,RegForm
from .serializer import EmbedSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages


# Create your views here.
def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://localhost:8000/myapp/reg')
            #return HttpResponse(r)
            json = r.json()
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'framerest/embeds.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'framerest/index.html', {'form': form})

def reform(request):  
    if request.method == "POST":  
        form = RegForm(request.POST)  
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            mobile_no=form.cleaned_data[' mobile_no']  
            password=form.cleaned_data['password']
            con_password=form.cleaned_data['con_password']
            registers=Registrationform(first_name=first_name,last_name=last_name,email=email,mobile_no= mobile_no,password=password,con_password=con_password)
            registers.save()
            messages.success(request,'user registrations sucessfull')
            return HttpResponseRedirect('/registrations/')
    else:
        form=RegForm()
    return render(request,'framerest/reg.html',{'frm':form})         

           
