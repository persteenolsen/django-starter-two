from django.shortcuts import render, redirect

# 10-12-2025 - For protecting the views by login
from django.contrib.auth.decorators import login_required

from example.models.todo import Todo
from example.forms.todo import TodoForm

# List all Todos
def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'list_todos.html', {'todos': todos})

# Create a Todo
# 10-12-2025 - Protected by login
@login_required(login_url="/accounts/login/")
def create_todo(request):
    if request.method == 'POST':

         # Max 10 rows in the DB
        numberoftodos = Todo.objects.all().count()
        if numberoftodos < 10 :

           form = TodoForm(request.POST)
           if form.is_valid():
              form.save()
              return redirect('list_todos')
                           
        else:
            return render(request, 'create_todo.html', {'numberoftodos': numberoftodos})
    else:
        form = TodoForm()
    return render(request, 'create_todo.html', {'form': form})
   

# Update a Todo
# 10-12-2025 - Protected by login
@login_required(login_url="/accounts/login/")
def update_todo(request, todo_id):

   todo = Todo.objects.get(id=todo_id)
   if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            #temp = form.cleaned_data.get("task")
            
            form.save()
            return redirect('list_todos')
   else:
        form = TodoForm(instance=todo)
   return render(request, 'update_todo.html', {'form': form, 'todo': todo})


# Delete a Todo
# 10-12-2025 - Protected by login
@login_required(login_url="/accounts/login/")
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_todos')