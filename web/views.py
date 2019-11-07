from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from web.forms import RegisterForm


def index(request):
    return render(request, 'homepage.html', {'logged_in': request.user.is_authenticated})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web:register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            error = 'user not found'
            return render(request, 'login.html', {'error': error})
        else:
            login(request, user)
            redirect('web:homepage')
    else:
        return render(request, 'login.html', {'error': error})
