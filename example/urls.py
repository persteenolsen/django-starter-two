# example/urls.py
from django.urls import path

from example.views.alpha import index

from example.views.alpha import about

from example.views.alpha import me

from example.views.beta import blog

# 27-08-2025 - Outdated !
# from example.views.beta import employee

from example.views.beta import list_employees
from example.views.beta import create_employee
from example.views.beta import update_employee
from example.views.beta import delete_employee

from example.views.gamma import list_todos
from example.views.gamma import create_todo
from example.views.gamma import update_todo
from example.views.gamma import delete_todo

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),

    # 27-08-2025 - Outdated !
    # path('employee', employee),
    
    path('employees/', list_employees, name='list_employees'),
    path('employee-create/', create_employee, name='create_employee'),
    path('employee-update/<int:employee_id>/', update_employee, name='update_employee'),
    path('employee-delete/<int:employee_id>/', delete_employee, name='delete_employee'),

    path('todos/', list_todos, name='list_todos'),
    path('todo-create/', create_todo, name='create_todo'),
    path('todo-update/<int:todo_id>/', update_todo, name='update_todo'),
    path('todo-delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]