from django.urls import path
from .views import CoursesListView, CourseDetailView, CreateRequest


urlpatterns = [
    path('', CoursesListView.as_view(), name = "course-list"),
    path('course/id=<int:pk>', CourseDetailView.as_view(), name = "course-detail"),
    path('course/id=<int:pk>/join', CreateRequest.as_view(), name = "create-request"),
]