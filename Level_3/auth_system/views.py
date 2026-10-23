from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")

    else:
            form = RegistrationForm()

    return render(request, "auth_system/register.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "auth_system/dashboard.html")
