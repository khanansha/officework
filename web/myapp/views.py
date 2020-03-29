from django.shortcuts import render
from .models import Profile ,Registration ,Contact ,SavedEmbeds
from django.http import HttpResponse
from django.conf import settings
import requests
from .forms import SubmitEmbed
from .serializer import EmbedSerializer, RegistrationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST.get('username', '')
        first_name = request.POST.get('first_name', '')
        last_name= request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        state = request.POST.get('state', '')
        pincode= request.POST.get('pincode', '')
        registers = Registration(username=username, first_name=first_name, last_name=last_name, email=email, password=password, state=state, pincode=pincode)
        registers.save()
    return render(request, 'myapp/register.html')
    

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'myapp/contact.html')



def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
            json = r.json()
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'myapp/embeds.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'myapp/index.html', {'form': form})



@api_view(['GET', 'POST'])
def regist_list(request):
    """
    List all of registrations, or create a new registrations.
    """
    if request.method == 'GET':
        obj = Registration.objects.all()
        serializer = RegistrationSerializer(obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET', 'PUT', 'DELETE'])
def reg_detail(request, pk):
    """
    Retrieve, update or delete of registrations details.
    """
    try:
        snippet = Registration.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistrationSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegistrationSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)