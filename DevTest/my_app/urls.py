from django.contrib import admin
from django.urls import path , include
from my_app import views

urlpatterns = [
   
    path('', views.upload_file, name='upload_file'),
  
     
    path('export/', views.export_summary, name='export_summary'),
    

]