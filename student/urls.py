from django.urls import path
from . import views

urlpatterns=[
    path("dashboard/",views.dashboard),
    path("lectures/",views.lectures),
    path("lecturecat/",views.lecturecat),
    path("enotes/",views.enotes),
    path("category/",views.Mycategory),
    path("profile/",views.profile),
    path("signout/",views.signout),
    path("softwarekit/",views.software),
    path("task/",views.task),
    path("tsubmitted/",views.tsubmitted),
  
]