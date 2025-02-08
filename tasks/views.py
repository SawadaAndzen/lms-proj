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
        })
        return context

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        course = self.get_course()
        a_form = AnswerForm(request.POST, request.FILES)
        redirect_url = "task-detail" if course else "course-list"
     
        if a_form.is_valid():
            answer = a_form.save(commit=False)
            answer.user = request.user
            answer.task = task
            answer.save()

        return redirect(redirect_url, pk=course.pk, task_pk=task.pk) if course else redirect("course-list")