# example/urls.py
from django.urls import path

from example.views.alpha import index

from example.views.alpha import about

from example.views.alpha import me

from example.views.beta import blog

from example.views.employee import list_employees
from example.views.employee import create_employee
from example.views.employee import update_employee
from example.views.employee import delete_employee

from example.views.todo import list_todos
from example.views.todo import create_todo
from example.views.todo import update_todo
from example.views.todo import delete_todo

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),
    
    path('employees/', list_employees, name='list_employees'),
    path('employee-create/', create_employee, name='create_employee'),
    path('employee-update/<int:employee_id>/', update_employee, name='update_employee'),
    path('employee-delete/<int:employee_id>/', delete_employee, name='delete_employee'),

    path('todos/', list_todos, name='list_todos'),
    path('todo-create/', create_todo, name='create_todo'),
    path('todo-update/<int:todo_id>/', update_todo, name='update_todo'),
    path('todo-delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]