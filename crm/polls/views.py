from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from .forms import RegisterUserModel, LoginUser


# Create your views here.
def home(request):
    # return HttpResponse("User loggedin")
    return render(request, "polls/index.html")


def register(request):
    form = RegisterUserModel()

    if request.method == "POST":
        form = RegisterUserModel(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "polls/register.html", context=context)


def login(request):
    form = LoginUser()

    if request.method == "POST":
        form = LoginUser(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
            # return redirect("login")

    context = {"form": form}
    return render(request, "polls/login.html", context=context)


def logout(request):
    auth.logout(request)

    return redirect("login")
