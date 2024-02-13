from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    return render(request,"page_html/index.html")

def aboutus(request):
    
    return render(request,"page_html/about.html")

def contactus(request):
    
    return render(request,"page_html/contact.html")

def blog(request):
    
    return render(request,"page_html/blog.html")

def product(request):
    
    return render(request,"page_html/product.html")

def login(request):
    
    return render(request,"page_html/login.html")
