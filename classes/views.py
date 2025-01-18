from django.views.generic import DetailView, ListView
from .models import Class


class MyClassesListView(ListView):
    model = Class
    template_name = 'groups/list.html'
    context_object_name = 'groups'
    
    
class ClassDetailView(DetailView):
    model = Class
    template_name = 'groups/group.html'
    context_object_name = 'group'