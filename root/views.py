from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import CustomSignUpForm, CustomLoginForm, ProfileForm, CustomChangePasswordForm, CustomUserChangeForm
from .models import Profile


#AUTH
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
        
        return reverse('index')
    
    
#PROFILE
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
    
    
#USER CUSTOMIZATION
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