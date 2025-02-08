from django.db.models import OuterRef, Subquery, BooleanField, Value
from django.db.models.functions import Coalesce
from django.contrib.auth.models import User
from tasks.models import TaskAnswer, Grade
from classes.models import Class
from courses.models import CourseInstance
from tasks.models import InstanceTask


def answers_with_grades(request):
    if request.user.is_authenticated and request.user.role.filter(role="teacher").exists():
        teacher_classes = Class.objects.filter(teacher=request.user)
        students = User.objects.filter(students__in=teacher_classes)
        course_instances = CourseInstance.objects.filter(course__in=teacher_classes.values_list('course', flat=True))

        instance_task_subquery = InstanceTask.objects.filter(
            task=OuterRef('task'),
            user=OuterRef('user'),
            course_instance__in=course_instances
        ).values('is_done')[:1]

        answers = TaskAnswer.objects.filter(
            task__instancetask__course_instance__in=course_instances,
            user__in=students
        ).select_related("task", "user").annotate(
            is_done=Coalesce(Subquery(instance_task_subquery, output_field=BooleanField()), Value(False))
        ).order_by("-created_at").distinct()

        for answer in answers:
            grade = Grade.objects.filter(task=answer.task, user=answer.user).first()
            answer.grade_value = grade.grade if grade else None

        return {"global_answers": answers}
    
    return {"global_answers": []}