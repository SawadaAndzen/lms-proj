from django.views.generic import DetailView, ListView
from django.shortcuts import redirect
from django.db.models import Q
from .models import Class


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