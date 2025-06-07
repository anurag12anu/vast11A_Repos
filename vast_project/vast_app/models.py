from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    course=models.TextField()
    contact=models.IntegerField()

def __str__(self):
    return self.name
    
