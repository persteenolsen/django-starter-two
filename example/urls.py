# example/urls.py
from django.urls import path

from example.views import index

from example.views import about


from example.views import me


urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),
]