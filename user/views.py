from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime

# Create your views here.

def index(request):
    d={}
    if request.method=="POST":
        Name=request.POST.get("name")
        Mobile=request.POST.get("mob")
        Email=request.POST.get("email")
        Massage=request.POST.get("msg")

        tblcontact(name=Name, email=Email, mobile=Mobile, massage=Massage).save()
        return HttpResponse("<script>alert('Data save successfully');location.href='/index/'</script>")
    
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def team(request):
    data=tblteam.objects.all()
    n={"tea":data}
    return render(request,"team.html",n)

def gallery(request):
    data=tblgallery.objects.all()
    d={"gal":data}
    return render(request,"gallery.html",d)

def login(request):
    if request.method=="POST":
       email=request.POST.get("email")
       password=request.POST.get("passwd")
       x=tblregister.objects.all().filter(email=email,password=password)
       if x.count()==1:
           request.session["name"]=str(x[0].name)
           request.session["userpic"]=str(x[0].picture)
           b=x[0].batch
           if b:
                request.session["batch"]=str(x[0].batch.id)
           request.session["email"]=email
           return HttpResponse("<script>alert('You are login successfully..');location.href='/student/dashboard/'</script>")
       else:
           return HttpResponse("<script>alert('Your Email Id or Password is incorrect.');location.href='/student/dashboard/'</script>")
    return render(request,"login.html")

def dashboard(request):
    return render(request,"dashboard.html")

def register(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Mobile=request.POST.get("mob")
        Password=request.POST.get("passwd")
        Address=request.POST.get("address")
        Picture=request.FILES["fu"]
        tblregister(name=Name,email=Email,mobile=Mobile,password=Password,address=Address,picture=Picture,regdate=datetime.now().date()).save()
        return HttpResponse("<script>alert('You are Registered Successfully');location.href='/register/'</script>")
    return render(request,"register.html")



def logout(request):
    user=request.session.get("email")
    if user:
        del request.session["email"]
        return redirect("/login/")
    return render(request,"logout.html")

def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")







