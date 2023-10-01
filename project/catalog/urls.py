from  django.urls import path, re_path
from .views import *

urlpatterns = [
    path('catalog/', index),
    path('catalog/register', auth)
]
