from django.contrib import admin
from .models import Course, JoinRequest, CourseInstance


admin.site.register(Course)
admin.site.register(CourseInstance)
admin.site.register(JoinRequest)