# example/urls.py
from django.urls import path

from example.views.alpha import index

from example.views.alpha import about

from example.views.alpha import me

from example.views.beta import blog

from example.views.beta import employee

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),

    path('employee', employee),
]