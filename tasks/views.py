from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView
from courses.models import Course
from .models import Task, TaskAnswer
from .forms import CommentForm, AnswerForm


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = "task"

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs['task_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()

        related_courses = Course.objects.filter(modules__lessons__tasks=task).distinct()
        course = related_courses.first() if related_courses.exists() else None

        context["course"] = course
        context["comments"] = task.comment_set.all()
        context["comments_form"] = CommentForm()
        context["answers"] = task.taskanswer_set.all()
        context["answers_form"] = AnswerForm()

        return context

    def post(self, request, *args, **kwargs):
        c_form = CommentForm(request.POST, request.FILES)
        a_form = AnswerForm(request.POST, request.FILES)

        if c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.user = request.user
            comment.task = self.get_object()
            comment.created_at = timezone.now()
            comment.save()
            
            course = Course.objects.filter(modules__lessons__tasks=comment.task).distinct().first()

            return redirect("task-detail", pk=course.pk, task_pk=self.kwargs['task_pk']) if course else redirect("course-list")
            
        if a_form.is_valid():
            answer = a_form.save(commit=False)
            answer.user = request.user
            answer.task = self.get_object()
            answer.save()

            course = Course.objects.filter(modules__lessons__tasks=answer.task).distinct().first()

            return redirect("task-detail", pk=course.pk, task_pk=self.kwargs['task_pk']) if course else redirect("course-list")