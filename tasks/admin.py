from django.contrib import admin
from .models import Task, TaskAnswer, Comment

admin.site.register(Task)
admin.site.register(TaskAnswer)
admin.site.register(Comment)