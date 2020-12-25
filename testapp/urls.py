from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .api import *

urlpatterns = [
      path('register/', RegisterApi.as_view()),
      path('simple/', SimpleApi.as_view()),
]