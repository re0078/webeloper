from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

# Create your views here.
from web.forms import RegisterForm, CourseForm
from web.models import Course
from django.core.mail import send_mail

from webeloper import settings


def index(request):
    return render(request, 'homepage.html', {'logged_in': request.user.is_authenticated})


def register(request):
    errors = []
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        if len(User.objects.filter(username=username)) > 0:
            errors.append('نام کاربری شما در سیستم موجود است')
        if password1 != password2:
            errors.append('گذرواژه و تکرار گذرواژه یکسان نیستند')
        if form.is_valid():
            form.save()
            return redirect('web:register')
    else:
        form = RegisterForm()
    print(errors)
    return render(request, 'register.html',
                  {'form': form, 'errors': errors, 'logged_in': request.user.is_authenticated})


def login_user(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            error = 'user not found'
        else:
            login(request, user)
            return redirect('web:homepage')
    return render(request, 'login.html', {'error': error, 'logged_in': request.user.is_authenticated})


def contact_us(request):
    if request.method == 'POST':
        text = request.POST['text']
        if 10 <= len(text) <= 250:
            send_mail(request.POST['title'], text, settings.EMAIL_HOST_USER, ['webe19lopers@gmail.com'],
                      fail_silently=True)
            return redirect('web:successful_submit')
    return render(request, 'contact_us.html', {'logged_in': request.user.is_authenticated})


def successful_submit(request):
    return render(request, 'successful_submit.html', {'logged_in': request.user.is_authenticated})


def logout_user(request):
    logout(request)
    return redirect('web:homepage')


def panel(request):
    return render(request, 'panel.html',
                  {'logged_in': request.user.is_authenticated, 'admin': request.user.is_superuser})


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user, 'logged_in': request.user.is_authenticated})


def setting(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('web:profile')
    else:
        return render(request, 'setting.html', {'logged_in': request.user.is_authenticated})


def create_course(request):
    if request.method == 'POST':
        course = Course(department=request.POST['department'],
                        name=request.POST['name'],
                        course_number=request.POST['course_number'],
                        group_number=request.POST['group_number'],
                        teacher=request.POST['teacher'],
                        start_time=request.POST['start_time'],
                        end_time=request.POST['end_time'],
                        first_day=request.POST['first_day'],
                        second_day=request.POST['second_day'],
                        )
        course.save()
        return redirect('web:profile')
    else:
        form = CourseForm()
        return render(request, 'create_course.html', {'form': form, 'logged_in': request.user.is_authenticated})


def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'courses.html', {'all_courses': all_courses
        , 'logged_in': request.user.is_authenticated})
