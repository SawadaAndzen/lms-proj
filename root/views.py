from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomSignUpForm, CustomLoginForm


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