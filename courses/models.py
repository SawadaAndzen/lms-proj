from django.db import models
from modules.models import Module


class Course(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    modules = models.ManyToManyField(Module, null = True, blank = True)
    
    def __str__(self):
        return self.name