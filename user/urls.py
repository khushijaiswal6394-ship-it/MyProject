from django.urls import path
from . import views

urlpatterns = [
 path("",views.index),
 path("home/",views.index),
 path("about/",views.about),
 path("team/",views.team),
 path("gallery/",views.gallery),
 path("login/",views.login),
 path("register/",views.register),
 path("dashboard/",views.dashboard),
 
 path("logout/",views.logout),
 path("services/",views.services),
 path("contact/",views.contact),
 
 
 

]

