from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .api import *

urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('simple/', SimpleApi.as_view()),
    path('read/', ProductReadApi.as_view()),
    path('create', ProductCreateApi.as_view()),
    path('update/<int:pk>', ProductUpdateApi.as_view()),
    path('delete/<int:pk>/', ProductDeleteApi.as_view()),
]
