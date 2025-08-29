from django import forms
from example.models.todo import Todo
from example.models.employee import Employee

class TodoForm(forms.ModelForm):

    task = forms.CharField(error_messages={'max_length':'A Todo Task can only have 25 characters!',
                                           'required':'A Todo Task can not be empty!'})
    
    class Meta:
        model = Todo
        fields = ['task', 'completed']


class EmployeeForm(forms.ModelForm):

    name = forms.CharField(error_messages={'max_length':'The Name of an Employee can only have 25 characters!', 
                                           'required':'The Name of an Employee can not be empty!'})
    
    author = forms.CharField(error_messages={'max_length':'The Author of an Employee can only have 25 characters!', 
                                             'required':'The Author of an Employee can not be empty!'})
                                             
    profession = forms.CharField(error_messages={'max_length':'The Profession of an Employee can only have 25 characters!',
                                                 'required':'The Profession of an Employee can not be empty!'})

    class Meta:
        model = Employee
        fields = ['name', 'author', 'profession']