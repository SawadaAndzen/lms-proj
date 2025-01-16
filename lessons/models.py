from django.db import models
from tasks.models import Task


class Lesson(models.Model):
    name = models.CharField(max_length = 50)
    tasks = models.ManyToManyField(Task, null = True, blank = True)
    
    def __str__(self):
        return self.name