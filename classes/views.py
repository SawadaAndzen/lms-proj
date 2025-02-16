from django.views.generic import DetailView, ListView, View
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q
from .models import Class
from .forms import ClassForm


class MyClassesListView(ListView):
    model = Class
    template_name = 'groups/list.html'
    context_object_name = 'groups'
    
    def get_queryset(self):
        return Class.objects.filter(Q(teacher=self.request.user) | Q(students=self.request.user)).distinct()

    def dispatch(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            return redirect('course-list')
        return super().dispatch(request, *args, **kwargs)
    
    
class ClassDetailView(DetailView):
    model = Class
    template_name = 'groups/group.html'
    context_object_name = 'group'
    
    
class CreateClass(View):
    def post(self, request, *args, **kwargs):
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.save()
            form.save_m2m()
            
            messages.success(request, "Class created successfully!")
            
            return JsonResponse({
                'success': True,
                'id': new_class.id,
                'name': new_class.name,
                'course_name': new_class.course.name,
                'teacher_name': new_class.teacher.username,
                'students_count': new_class.students.count(),
                'students': list(new_class.students.values_list('id', flat=True)),
                'course_id': new_class.course.id,
                'teacher_id': new_class.teacher.id,
            })
        
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)


class UpdateClass(View):
    def post(self, request, *args, **kwargs):
        class_id = kwargs.get("pk")
        class_instance = get_object_or_404(Class, id=class_id)

        form = ClassForm(request.POST, instance=class_instance)
        if form.is_valid():
            updated_class = form.save(commit=False)
            updated_class.save()
            form.save_m2m()

            return JsonResponse({
                'success': True,
                'id': updated_class.id,
                'name': updated_class.name,
                'course_name': updated_class.course.name,
                'students': list(updated_class.students.values_list('id', flat=True)),
            })
        
        return HttpResponseBadRequest(JsonResponse({'success': False, 'errors': form.errors}))


class DeleteClass(View):
    def post(self, request, pk, *args, **kwargs):
        class_instance = get_object_or_404(Class, id=pk)
        class_instance.delete()

        return JsonResponse({'success': True})