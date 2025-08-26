from django import forms
from example.models.todo import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'completed']