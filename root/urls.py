from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import Forum, ToggleTaskStatusView, AddGradeView, Index
from .views import SignUpView, CustomLoginView, CustomPasswordView, UserUpdate
from .views import ProfileDetailView, UpdateProfileView, ProfileAPI, AddCashView
from .views import AcceptJoinRequestView, DeclineJoinRequestView, CreateRole, DeleteRole, UpdateRole


urlpatterns = [
    path('', Index.as_view(), name = "index"),
    #AUTH
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    #FORUM
    path('forum/', Forum.as_view(), name = 'forum'),
    #TEACHER FEAT.
    path('add-grade/', AddGradeView.as_view(), name='add-grade'),
    path('toggle-task-status/', ToggleTaskStatusView.as_view(), name='toggle-task-status'),
    #PROFILE
    path('profile/<str:username>', ProfileDetailView.as_view(), name = 'profile'),
    path('profile/<str:username>/update/', UpdateProfileView.as_view(), name = 'update-profile'),
    path('users/update/<str:username>/data/', UserUpdate.as_view(), name = 'user-update'),
    path("users/update/<str:username>/data/password/", CustomPasswordView.as_view(), name = "change-password"),
    path("add-cash/", AddCashView.as_view(), name="add-cash"),
    #ADMIN FEAT.
    path('join-request/accept/<int:pk>/', AcceptJoinRequestView.as_view(), name='accept_join_request'),
    path('join-request/decline/<int:pk>/', DeclineJoinRequestView.as_view(), name='decline_join_request'),
    path('role/create/', CreateRole.as_view(), name='create-role'),
    path('role/edit/<int:pk>/', UpdateRole.as_view(), name='edit-role'),
    path('role/delete/<int:pk>/', DeleteRole.as_view(), name='delete-role'),
    #API
    path("api/profile/all/", ProfileAPI.as_view(), name = "profile-api"),
]