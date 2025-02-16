from django.db.models import OuterRef, Subquery, BooleanField, Value, IntegerField
from django.db.models.functions import Coalesce
from django.contrib.auth.models import User
from tasks.models import TaskAnswer, Grade
from classes.models import Class
from courses.models import CourseInstance, JoinRequest, Course
from tasks.models import InstanceTask
from .models import Role


def answers_with_grades(request):
    if request.user.is_authenticated and request.user.role.filter(role="teacher").exists():
        print(f"LOG: @{request.user.username} is a teacher!")
        
        teacher_classes = Class.objects.filter(teacher=request.user)
        students = User.objects.filter(students__in=teacher_classes)
        course_instances = CourseInstance.objects.filter(course__in=teacher_classes.values_list('course', flat=True))

        instance_task_subquery = InstanceTask.objects.filter(
            task=OuterRef('task'),
            user=OuterRef('user'),
            course_instance__in=course_instances
        ).values('is_done')[:1]

        grade_subquery = Grade.objects.filter(
            task=OuterRef('task'),
            user=OuterRef('user')
        ).values('grade')[:1]

        answers = TaskAnswer.objects.filter(
            task__instancetask__course_instance__in=course_instances,
            user__in=students
        ).select_related("task", "user").annotate(
            is_done=Coalesce(Subquery(instance_task_subquery, output_field=BooleanField()), Value(False)),
            grade_value=Coalesce(Subquery(grade_subquery), Value(None))
        ).order_by("-created_at").distinct()

        return {"global_answers": answers}
    
    elif request.user.is_authenticated and request.user.role.filter(role="admin").exists():
        print(f"LOG: @{request.user.username} is an admin!")
        
        join_requests = JoinRequest.objects.all().distinct()
        classes = Class.objects.all().distinct()
        teachers = User.objects.filter(role__role='teacher')
        students = User.objects.filter(role__role='student')
        courses = Course.objects.all()
        
        users = User.objects.filter(role__isnull=False).distinct()
        all_users = User.objects.all().distinct()
        
        return {"join_requests": join_requests, "classes": classes, 
                "teachers": teachers, "students": students, "courses": courses,
                "users": users, "all_users": all_users,}
    
    return {"global_answers": [], "join_requests": [], "classes": [],
            "teachers": [], "students": [], "courses": [], "users": [],
            "all_users": [],}