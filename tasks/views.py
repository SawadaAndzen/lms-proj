from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from courses.models import Course
from .models import Task, TaskAnswer, Grade
from .forms import AnswerForm


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = "task"

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs['task_pk'])

    def get_course(self):
        return Course.objects.filter(modules__lessons__tasks=self.get_object()).distinct().first()

    def get_global_answers(self):
        return TaskAnswer.objects.filter(task=self.get_object()).select_related("user").annotate(
            grade_value=Coalesce(
                Subquery(
                    Grade.objects.filter(
                        task=OuterRef('task'),
                        user=OuterRef('user')
                    ).values('grade')[:1]
                ), 
                Value(None)
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        course = self.get_course()

        is_teacher = self.request.user.role.filter(role="teacher").exists()

        answers = task.taskanswer_set.filter(user=self.request.user)
        context.update({
            "course": course,
            "answers": answers,
            "answers_form": AnswerForm(),
            "is_teacher": is_teacher,
            "global_answers": self.get_global_answers(),
        })
        return context