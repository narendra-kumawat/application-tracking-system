from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from CVAnalyzer import views

urlpatterns = [
    path('pdf', views.PDF.as_view()),
    path('docx', views.Docx.as_view()),
    path('checkapi', views.CheckAPI.as_view()),
    path('apply-for-job', views.InsertEmployeeDetails.as_view()),
    path('job-description', views.InsertJobDescription.as_view())
] 