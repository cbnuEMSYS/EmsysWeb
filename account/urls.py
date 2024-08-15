from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('logout', test , name = 'logout'),
    path('login', test , name = 'login'),
    path('register', test, name = 'register'),
]