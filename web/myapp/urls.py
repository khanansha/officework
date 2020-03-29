
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views
urlpatterns = [
    path("" ,views.register , name='register'),
    path("contact/", views.contact, name="ContactUs"),
    path("rest/", views.save_embed, name="save_embed"),
    path("reg/", views.regist_list, name="reg_list"),
    path('reg/<int:pk>', views.reg_detail, name="reg_details"),
    
]