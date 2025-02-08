from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, View
from tasks.models import TaskAnswer, Grade
from .forms import CustomSignUpForm, CustomLoginForm, ProfileForm, CustomChangePasswordForm, CustomUserChangeForm
from .models import Profile
from .serializers import ProfileSerializer


class Index(TemplateView):
    template_name = "root/index.html"


class SignUpView(CreateView):
    model = User
    form_class = CustomSignUpForm
    template_name = "auth/signup.html"
    success_url = "/login/"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['success_message'] = "Succes regestration!"
        
        return response
    
    
class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    form_class = CustomLoginForm
    
    def get_success_url(self):
        self.request.session['success_message'] = f"Hi, {self.request.user.username}!"
        
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
    
    
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'root/profile/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        username = self.kwargs.get('username', self.request.user.username)
        user = User.objects.get(username=username)
        profile, created = Profile.objects.get_or_create(user=user)
        
        self.request.session['last_viewed'] = profile.id
        
        return profile


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'root/profile/update_profile.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.object.user.username})

    def get_object(self, queryset = None):
        user = self.request.user
        profile, created = Profile.objects.get_or_create(user=user)
        
        return profile

    def form_valid(self, form):
        profile = form.save(commit = False)
        profile.user = self.request.user
        profile.save()
        
        if not profile.pfp:
            profile.pfp = 'static/profile/default-pfp.jpg'
        profile.save()
        
        self.request.session['success_message'] = 'Success'
        
        del self.request.session['success_message']
        
        return super().form_valid(form)
    
    
class UserUpdate(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'root/user/change_user.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.object.username})
    
    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        
        return User.objects.get(username = username)
    
    
class CustomPasswordView(PasswordChangeView):
    template_name = 'root/user/change_password.html'
    form_class = CustomChangePasswordForm
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
    
    
class AddGradeView(View):
    def post(self, request, *args, **kwargs):
        answer_id = request.POST.get("answer_id")
        grade_value = request.POST.get("grade")

        answer = get_object_or_404(TaskAnswer, id=answer_id)
        grade, created = Grade.objects.update_or_create(
            task=answer.task, 
            user=answer.user, 
            defaults={"grade": grade_value}
        )

        return JsonResponse({
            'success': True,
            'grade': grade.grade,
            'answer_id': answer.id
        })

    
class ProfileAPI(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer