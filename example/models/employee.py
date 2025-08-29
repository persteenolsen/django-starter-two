from django.db import models

# from django.core.validators import MaxLengthValidator

class Employee(models.Model):
    
    # name = models.CharField(max_length=25, validators=[MaxLengthValidator(limit_value=25)])
    # 29-08-2025 - The validation with messages is handled in the Form
    name = models.CharField(max_length=25)

    # author = models.CharField(max_length=25,default='Admin', validators=[MaxLengthValidator(limit_value=25)])
    # 29-08-2025 - The validation with messages is handled in the Form
    author = models.CharField(max_length=25,default='Admin')

    # profession = models.CharField(max_length=25, validators=[MaxLengthValidator(limit_value=25)])
    # 29-08-2025 - The validation with messages is handled in the Form
    profession = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name