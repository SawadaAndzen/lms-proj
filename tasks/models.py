from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length = 50)
    desc = models.TextField()
    media = models.FileField(upload_to = 'tasks/files/', null = True, blank = True)
    is_done = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
    
    
class TaskAnswer(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    media = models.FileField(upload_to = 'tasks/answers/', blank = True, null = True)
    
    def __str__(self):
        return f"@{self.user.username}'s answer for {self.task}"
    
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    media = models.FileField(upload_to = "tasks/comments/", blank = True, null = True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Comment by {self.user} for the task: {self.task}"