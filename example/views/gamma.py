from django.shortcuts import render, redirect

from example.models.todo import Todo

# List all Todos
def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'list_todos.html', {'todos': todos})

# Create a new Todo
def create_todo(request):
    if request.method == 'POST':

        # Max 10 rows in the DB
        numberoftodos = Todo.objects.all().count()
        if numberoftodos < 10 :
           task = request.POST['task']
           Todo.objects.create(task=task)
           return redirect('list_todos')
        return render(request, 'create_todo.html', {'numberoftodos': numberoftodos})
    return render(request, 'create_todo.html')

# Update a Todo
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.task = request.POST['task']

         # 24-08-2025 - Working :-)
        todo.completed = 'completed' in request.POST
        
        # 24-08-2025 - Not Working
        #todo.completed = request.POST['completed']

        todo.save()
        return redirect('list_todos')
    return render(request, 'update_todo.html', {'todo': todo})

# Delete a Todo
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_todos')