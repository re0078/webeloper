from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from web.forms import RegisterForm


def index(request):
    return render(request, 'homepage.html', )


def register(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            last_name = form.cleaned_data.get('last_name')
            first_name = form.cleaned_data.get('first_name')
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            user = authenticate(first_name=first_name,
                                last_name=last_name,
                                username=username,
                                password1=password1,
                                password2=password2,
                                email=email)
            login(request, user)
            return redirect('web:homepage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
