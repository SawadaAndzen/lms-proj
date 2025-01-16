from django.db import models
from django.contrib.auth.models import User
from root.models import Role


class Class(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    course = ...
    teacher = models.ForeignKey(
        User, 
        on_delete = models.SET_NULL, 
        null = True, 
        limit_choices_to = {'role__role': 'teacher'},
        related_name = "teacher"
    )
    students = models.ManyToManyField(
        User, 
        blank = True, 
        limit_choices_to = {'role__role': 'student'},
        related_name = "students"
    )
    
    def __str__(self):
        return self.name