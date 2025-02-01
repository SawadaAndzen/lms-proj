from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.views.generic.edit import CreateView
from root.models import Profile
from .models import JoinRequest, Course


class CoursesListView(ListView):
    model = Course
    template_name = 'courses/list.html'
    context_object_name = 'courses'
    #paginate_by = 9
    
    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
    

class CourseView(DetailView):
    model = Course
    template_name = "courses/course.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        course = self.get_object()
        total_tasks = 0
        completed_tasks = 0

        for module in course.modules.all():
            for lesson in module.lessons.all():
                total_tasks += lesson.tasks.count()
                completed_tasks += lesson.tasks.filter(is_done=True).count()

        progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        context["progress"] = int(progress)
        
        return context


class CreateRequest(CreateView):
    model = JoinRequest

    def post(self, request, *args, **kwargs):
        course_id = self.kwargs.get('pk')
        course = get_object_or_404(Course, id=course_id)
        profile = get_object_or_404(Profile, user=request.user)

        if profile.cash >= course.price:
            profile.cash -= course.price
            profile.save()

            JoinRequest.objects.create(user=request.user, course=course)

            messages.success(request, "Course join request pent successfully!")
            
        else:
            messages.error(request, "Insufficient balance to join this course.")
        
        return HttpResponseRedirect(reverse('course-list'))
    
    
class FilteredCourses(View):
    def get(self, request, min_price, max_price, *args, **kwargs):
        courses = Course.objects.filter(price__gte=min_price, price__lte=max_price).values("id", "name", "desc", "price")
        
        return JsonResponse(list(courses), safe=False)