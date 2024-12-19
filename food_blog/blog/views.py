from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index page")

def profile(request):
    return HttpResponse("This is the profile page")

def register(request):
    return HttpResponse("This is the registration page")

def login(request):
    return HttpResponse("This is the login page")