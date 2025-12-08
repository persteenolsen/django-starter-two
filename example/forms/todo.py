from django import forms
from example.models.todo import Todo

class TodoForm(forms.ModelForm):

    task = forms.CharField(error_messages={'max_length':'A Todo Task can only have 25 characters!',
                                           'required':'A Todo Task can not be empty!'})
    
    class Meta:
        model = Todo
        fields = ['task', 'completed']
