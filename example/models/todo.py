from django.db import models
from django.core.validators import MaxLengthValidator

class Todo(models.Model):

    task = models.CharField(max_length=25, validators=[MaxLengthValidator(limit_value=25)])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task