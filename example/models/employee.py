from django.db import models

class Employee(models.Model):
    
    name = models.CharField(max_length=100)
    
    # This field was added when the program was already in use and in production
    author = models.CharField(max_length=100,default='Admin')

    profession = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name