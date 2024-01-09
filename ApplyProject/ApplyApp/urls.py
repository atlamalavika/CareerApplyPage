from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('get/',home),
    path('',postData),
    # path('User/',post_User),
]