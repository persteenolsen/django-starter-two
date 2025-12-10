
# Working with models
from django.shortcuts import render, redirect

# 10-12-2025 - For protecting the views by login
from django.contrib.auth.decorators import login_required

from example.models.employee import Employee

from example.forms.employee import EmployeeForm

# List all Employees
def list_employees(request):
    # employees = Employee.objects.all()
    employees = Employee.objects.all().order_by('name')
    return render(request, 'list_employees.html', {'employees': employees})

# Create an Employee
# 10-12-2025 - Protected by login
@login_required(login_url="/accounts/login/")
def create_employee(request):
    if request.method == 'POST':

         # Max 10 rows in the DB
        numberofemployees = Employee.objects.all().count()
        if numberofemployees < 10 :

           form = EmployeeForm(request.POST)
           if form.is_valid():
              form.save()
              return redirect('list_employees')
                           
        else:
            return render(request, 'create_employee.html', {'numberofemployees': numberofemployees})
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})
   

# Update a Employee
# 10-12-2025 - Protected by login
@login_required(login_url="/accounts/login/")
def update_employee(request, employee_id):

   employee = Employee.objects.get(id=employee_id)
   if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            #temp = form.cleaned_data.get("task")
            
            form.save()
            return redirect('list_employees')
   else:
        form = EmployeeForm(instance=employee)
   return render(request, 'update_employee.html', {'form': form, 'employee': employee})

# Delete a Employee

# 10-12-2025 - Protected by login
@login_required(login_url="/accounts/login/")
def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('list_employees')