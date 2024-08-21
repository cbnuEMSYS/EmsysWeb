from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('board_list', board_list, name = 'board_list'),
]