from django.contrib import admin
from .models import Task, TaskAnswer, Comment, InstanceTask, Grade

admin.site.register(Task)
admin.site.register(InstanceTask)
admin.site.register(TaskAnswer)
admin.site.register(Comment)
admin.site.register(Grade)