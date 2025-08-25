# example/urls.py
from django.urls import path

from example.views.alpha import index

from example.views.alpha import about

from example.views.alpha import me

from example.views.beta import blog

from example.views.beta import employee

from example.views.gamma import list_todos
from example.views.gamma import create_todo
from example.views.gamma import update_todo
from example.views.gamma import delete_todo

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),

    path('employee', employee),

    path('todos/', list_todos, name='list_todos'),
    path('create/', create_todo, name='create_todo'),
    path('update/<int:todo_id>/', update_todo, name='update_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]