from django.db import models
from django.core.validators import MaxLengthValidator

class Todo(models.Model):

    # 25-08-2025 - The error message is not displayed in template but everything else works fine
    task = models.CharField(max_length=25,
                            validators=[MaxLengthValidator(limit_value=25,
                                                           message="The Todo is too long !")])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task