from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from web.forms import RegisterForm


def index(request):
    return render(request, 'homepage.html', )


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web:homepage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    return render(request, 'login.html',)
