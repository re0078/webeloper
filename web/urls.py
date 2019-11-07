from django.urls import path, include

from web.views import index

urlpatterns = [
    path('', index, name='homepage')
]
