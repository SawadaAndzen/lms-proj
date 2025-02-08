from django.contrib import admin
from .models import Task, TaskAnswer, InstanceTask, Grade

admin.site.register(Task)
admin.site.register(InstanceTask)
admin.site.register(TaskAnswer)
admin.site.register(Grade)