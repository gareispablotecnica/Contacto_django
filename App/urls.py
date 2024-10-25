from django.urls import path
from .views import *
urlpatterns = [
    path('',Home,name='inicio'),
    path('gmail',Gmail,name='gmail'),
]