from django.urls import path, include

from web.views import index, register, login

app_name = "web"
urlpatterns = [
    path('', index, name='homepage'),
    path('register', register, name='register'),
    path('login', login, name='login'),
]
