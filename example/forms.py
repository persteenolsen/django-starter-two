from django import forms
from example.models.todo import Todo
from example.models.employee import Employee

class TodoForm(forms.ModelForm):

    task = forms.CharField(error_messages={'max_length':'A Todo Task can only have 25 characters!'})
    
    class Meta:
        model = Todo
        fields = ['task', 'completed']


class EmployeeForm(forms.ModelForm):

    name = forms.CharField(error_messages={'max_length':'A Employee Name can only have 25 characters!'})
    
    author = forms.CharField(error_messages={'max_length':'A Employee Author can only have 25 characters!'})

    profession = forms.CharField(error_messages={'max_length':'A Employee Profession can only have 25 characters!'})

    class Meta:
        model = Employee
        fields = ['name', 'author', 'profession']