from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from root.models import Profile
from .models import JoinRequest, Course


class CoursesListView(ListView):
    model = Course
    template_name = 'courses/list.html'
    context_object_name = 'courses'
    
    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


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