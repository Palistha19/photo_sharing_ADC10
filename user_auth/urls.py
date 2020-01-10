from django.urls import path
from .views import *

urlpatterns=[
    path("login",get_login_page)
]