# example/urls.py
from django.urls import path

from example.views import index

from example.views import about


urlpatterns = [
    
    path('', index),
    
    path('about', about),
]