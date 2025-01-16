from django.db import models
from lessons.models import Lesson


class Module(models.Model):
    name = models.CharField(max_length = 50)
    lessons = models.ManyToManyField(Lesson, blank = True, null = True)
    
    def __str__(self):
        return self.name