from django.contrib import admin
from .models import Task, TaskAnswer

admin.site.register(Task)
admin.site.register(TaskAnswer)