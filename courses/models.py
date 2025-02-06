from django.db import models
from django.contrib.auth.models import User
from modules.models import Module


class Course(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    modules = models.ManyToManyField(Module, blank = True)
    price = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0)
    
    def __str__(self):
        return self.name
    
    
class CourseInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}'s {self.course.name} instance"


class JoinRequest(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'@{self.user.username} wants to join {self.course.name}'