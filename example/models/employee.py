from django.db import models
from django.core.validators import MaxLengthValidator

class Employee(models.Model):
    
    name = models.CharField(max_length=25, validators=[MaxLengthValidator(limit_value=25)])
    
    author = models.CharField(max_length=25,default='Admin', validators=[MaxLengthValidator(limit_value=25)])

    profession = models.CharField(max_length=25, validators=[MaxLengthValidator(limit_value=25)])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name