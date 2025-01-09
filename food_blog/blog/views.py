from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

def index(request):
    return render(request, "blog/index.html")

def profile(request):
    return HttpResponse("This is the profile page")

def register(request):
    return render(request, "blog/register.html")

def login(request):
    return render(request, "blog/login.html")