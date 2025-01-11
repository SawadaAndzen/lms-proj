from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import SignUpView, CustomLoginView


urlpatterns = [
    path('', TemplateView.as_view(template_name = "root/index.html"), name = "index"),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
]