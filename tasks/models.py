from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    media = models.FileField(upload_to = 'tasks/files/', null = True, blank = True)
    
    def __str__(self):
        return self.name
    
    
class InstanceTask(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course_instance = models.ForeignKey('courses.CourseInstance', on_delete = models.CASCADE)
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    is_done = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.username}'s task: {self.task.name}"
    
    
class TaskAnswer(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    media = models.FileField(upload_to = 'tasks/answers/', blank = True, null = True)
    created_at = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return f"@{self.user.username}'s answer for {self.task}"
    
    
class Grade(models.Model):
    GRADE_CHOICES = [(i, str(i)) for i in range(1, 6)] # - from 1 to 5
    
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    grade = models.PositiveIntegerField(choices = GRADE_CHOICES)
    
    def __str__(self):
        return f"@{self.user.username} - {self.task} ({self.grade})"
    
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    media = models.FileField(upload_to = "tasks/comments/", blank = True, null = True)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"Comment by @{self.user} for the task: {self.task}"