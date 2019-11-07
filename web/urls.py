from django.urls import path, include

from web.views import index, register, login_user

app_name = "web"
urlpatterns = [
    path('', index, name='homepage'),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
]
