from django.shortcuts import render,redirect

from django.http import HttpResponse
from user.models import *

# Create your views here.
def dashboard(request):
    return render(request,"student/dashboard.html")

def Mycategory(request):
    return render(request,"student/category.html")

def lecturecat(request):
    bid=request.session.get("batch")
    cat=category.objects.all().filter(batch_name=bid)
    #cat=category.objects.all()
    d={"categories":cat}
    return render(request,"student/lecturecat.html",d)

def lectures(request):
    x=request.GET.get("cid")
    if x:
        data=mylecture.objects.all().filter(category=x)
    else:
        data=mylecture.objects.all().order_by("-id")
    d={"vdo":data}
    return render(request,"student/lectures.html",d)

def enotes(request):
    bid=request.session.get("batch")
    data=notes.objects.all().filter(batch=bid)
    d={"notes":data}
    return render(request,"student/enotes.html",d)

def profile(request):
    user=request.session.get("email")
    data=tblregister.objects.all().filter(email=user)
    d={"userinfo":data}
    return render(request,"student/profile.html",d)
def signout(request):
    user=request.session.get("email")
    if user:
        del request.session["name"]
        del request.session["userpic"]
        del request.session["email"]
        return redirect("/login/")
    return render(request,"student/signout.html")

def software(request):
    data=softwarekit.objects.all().order_by("-id")
    d={"sdata":data}
    return render(request,"student/softwarekit.html",d)

def task(request):
    bid=request.session.get("batch")
    data=mytask.objects.all().filter(batch=bid)
    d={"data":data}
    return render(request,"student/task.html",d)
def tsubmitted(request):
    userid = request.session.get("email")

    if request.method == "POST":
        title = request.POST.get("title")
        tid = request.POST.get("tid")
        taskfile = request.FILES.get("fu")

        x = submittedtask.objects.filter(userid=userid, tid=tid).count()

        if x == 1:
            return HttpResponse(
                "<script>alert('This task is already submitted..');location.href='/student/task/'</script>"
            )
        else:
            submittedtask.objects.create(
                userid=userid,
                tid=tid,
                title=title,
                upload_task=taskfile   # ✅ CORRECT FIELD NAME
            )
            return HttpResponse(
                "<script>alert('Task submitted successfully');location.href='/student/task/'</script>"
            )

    return render(request, "student/tsubmitted.html")


    