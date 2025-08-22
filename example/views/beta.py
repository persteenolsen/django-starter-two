
# Working with models
from django.shortcuts import render

from example.models.post import Post

from example.models.employee import Employee

def blog(request):
    
    # 06-08-2025 - The below statement is equal to the SQL:
    # Select * from Post order by created_at DESC
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog.html', {'posts': posts})

def employee(request):
    
    # 22-08-2025 - The below statement is equal to the SQL:
    # Select * from Employee order by name ASC
    employees = Employee.objects.all().order_by('name')

    return render(request, 'employees.html', {'employees': employees})