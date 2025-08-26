from django.shortcuts import render, redirect

from example.models.todo import Todo
from example.forms import TodoForm

# List all Todos
def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'list_todos.html', {'todos': todos})


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
def update_todo(request, todo_id):

   todo = Todo.objects.get(id=todo_id)
   if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list_todos')
   else:
        form = TodoForm(instance=todo)
   return render(request, 'update_todo.html', {'form': form, 'todo': todo})

# Delete a Todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_todos')