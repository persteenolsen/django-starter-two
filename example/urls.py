# example/urls.py
from django.urls import path

from example.views import index

from example.views import about

from example.views import me

from example.views import blog

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),
]