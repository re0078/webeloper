from django.urls import path, include

from web.views import index, register, login_user, contact_us, successful_submit, logout_user, panel, profile, setting, \
    create_course, courses, add_course

app_name = "web"
urlpatterns = [
    path('', index, name='homepage'),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('contact_us', contact_us, name='contact_us'),
    path('successful_submit', successful_submit, name='successful_submit'),
    path('logout', logout_user, name='logout'),
    path('panel', panel, name='panel'),
    path('profile', profile, name='profile'),
    path('setting', setting, name='setting'),
    path('create_course', create_course, name='create_course'),
    path('courses', courses, name='courses'),
    path('add_course', add_course, name='add_course'),
]
