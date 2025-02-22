from django.db import models
from django.contrib.auth.models import User
from root.models import Role
from courses.models import Course


class Class(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True)
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
        related_name="class_students"
    )
    
    def __str__(self):
        return self.name