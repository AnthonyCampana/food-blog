from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import registrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout 
from django.contrib.auth import login as auth_login

def index(request):
    return render(request, "blog/index.html")

def profile(request):
    return HttpResponse("This is the profile page")

def register(request):

    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(form.cleaned_data["userName"], form.cleaned_data["email"], form.cleaned_data["password"])
            new_user.save()
            HttpResponseRedirect("/")

    form = registrationForm() 
    return render(request, "blog/register.html", {"form": form})

def login(request):
    print(request.method)
    if request.method == "POST":
        password = request.POST["password"]
        username = request.POST["userName"]

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user=user)
            return render(request, "blog/index.html")
    else:
        print("inside the login template")
        form = LoginForm()
        return render(request, "blog/login.html", {"form": form})

def logout(request):
    auth_logout(request)
    return render(request, "blog/index.html")
