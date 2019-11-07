from django.urls import path, include

from web.views import index, register, login_user, contact_us, successful_submit

app_name = "web"
urlpatterns = [
    path('', index, name='homepage'),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('contact_us', contact_us, name='contact_us'),
    path('successful_submit', successful_submit, name='successful_submit'),
]
