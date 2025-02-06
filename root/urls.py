from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import SignUpView, CustomLoginView, CustomPasswordView, UserUpdate, ProfileDetailView, UpdateProfileView, ProfileAPI


urlpatterns = [
    path('', TemplateView.as_view(template_name = "root/index.html"), name = "index"),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('profile/<str:username>', ProfileDetailView.as_view(), name = 'profile'),
    path('profile/<str:username>/update/', UpdateProfileView.as_view(), name = 'update-profile'),
    path('users/update/<str:username>/data/', UserUpdate.as_view(), name = 'user-update'),
    path("users/update/<str:username>/data/password/", CustomPasswordView.as_view(), name = "change-password"),
    path("api/profile/all/", ProfileAPI.as_view(), name = "profile-api"),
]