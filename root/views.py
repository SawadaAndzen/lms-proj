from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from decimal import Decimal
from courses.models import CourseInstance, JoinRequest
from tasks.models import TaskAnswer, Grade, InstanceTask
from .forms import MessageForm, CustomSignUpForm, CustomLoginForm
from .forms import ProfileForm, CustomChangePasswordForm, CustomUserChangeForm, RoleForm
from .models import Profile, Message, Role
from .serializers import ProfileSerializer
from .mixins import SecureMixin

import json


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
    
    
class ProfileDetailView(SecureMixin, DetailView):
    model = Profile
    template_name = 'root/profile/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        username = self.kwargs.get('username', self.request.user.username)
        user = User.objects.get(username=username)
        profile, created = Profile.objects.get_or_create(user=user)
        
        self.request.session['last_viewed'] = profile.id
        
        return profile


class UpdateProfileView(SecureMixin, UpdateView):
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
    
    
class UserUpdate(SecureMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'root/user/change_user.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.object.username})
    
    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        
        return User.objects.get(username = username)
    
    
class CustomPasswordView(SecureMixin, PasswordChangeView):
    template_name = 'root/user/change_password.html'
    form_class = CustomChangePasswordForm
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
    
    
class Forum(SecureMixin, ListView):
    model = Message
    template_name = "root/forum.html"
    context_object_name = 'messages'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({"messages_form": MessageForm(),})

        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)

        if form.is_valid():
            mss = form.save(commit=False)
            mss.user = request.user
            mss.created_at = timezone.now()
            mss.save()
            
        return redirect('forum')
    
    
class AddGradeView(SecureMixin, View):
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


class ToggleTaskStatusView(SecureMixin, View):
    def post(self, request, *args, **kwargs):
        if not request.user.role.filter(role="teacher").exists():
            return JsonResponse({'success': False, 'message': 'Permission denied'}, status=403)

        try:
            data = json.loads(request.body)
            answer_id = data.get('answer_id')

            answer = TaskAnswer.objects.get(id=answer_id)

            instance_task = InstanceTask.objects.get(
                task=answer.task,
                user=answer.user
            )

            instance_task.is_done = not instance_task.is_done
            instance_task.save()

            return JsonResponse({'success': True, 'is_done': instance_task.is_done})

        except (InstanceTask.DoesNotExist, TaskAnswer.DoesNotExist):
            return JsonResponse({'success': False, 'message': 'Task not found'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)


class AcceptJoinRequestView(SecureMixin, View):
    def post(self, request, pk, *args, **kwargs):
        join_request = get_object_or_404(JoinRequest, pk=pk)
        
        CourseInstance.objects.create(user=join_request.user, course=join_request.course)
        
        join_request.delete()
        
        return JsonResponse({"success": True})


class DeclineJoinRequestView(SecureMixin, View):
    def post(self, request, pk, *args, **kwargs):
        join_request = get_object_or_404(JoinRequest, pk=pk)
        student_profile = get_object_or_404(Profile, user=join_request.user)
        
        with transaction.atomic():
            student_profile.cash += join_request.course.price
            student_profile.save()
            join_request.delete()
        
        return JsonResponse({"success": True})
    
    
class CreateRole(SecureMixin, View):
    def post(self, request, *args, **kwargs):
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            
            return JsonResponse({"success": True})
        
        return JsonResponse({"success": False, "errors": form.errors}, status=400)


class UpdateRole(SecureMixin, View):
    def post(self, request, pk, *args, **kwargs):
        role = get_object_or_404(Role, id=pk)
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            
            return JsonResponse({"success": True})
        
        return JsonResponse({"success": False, "errors": form.errors}, status=400)


class DeleteRole(SecureMixin, View):
    def post(self, request, pk, *args, **kwargs):
        role = get_object_or_404(Role, id=pk)
        role.delete()
        
        return JsonResponse({"success": True})
    
    
class AddCashView(SecureMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            profile = get_object_or_404(Profile, user=request.user)
            amount = Decimal(request.POST.get("amount", 0))

            if amount <= 0:
                return JsonResponse({"success": False, "message": "Invalid amount!"}, status=400)

            profile.cash += amount
            profile.save()

            return JsonResponse({"success": True, "message": "Cash added successfully!", "new_balance": profile.cash})

        except ValueError:
            return JsonResponse({"success": False, "message": "Invalid input!"}, status=400)
    
    
class ProfileAPI(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]