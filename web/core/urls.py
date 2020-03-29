from django.urls import path
from .import views
# SET THE NAMESPACE!
app_name = 'core'
urlpatterns = [
    path("" ,views.register , name='save_embed'),
    path("index/" ,views.index , name='login'),
    path("special/" ,views.special , name='login'),
    path("logout/" ,views.user_logout , name='login'),
    path("register/" ,views.register , name='login'),
    path("log/" ,views.login , name='login'),
    path("logg/" ,views.user_login , name='login'),
    path("signup/" ,views.signup , name='login'),



    







]