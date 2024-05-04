from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('empform',views.empform,name='empform'),
    path('empdata',views.empdata,name='empdata')
]