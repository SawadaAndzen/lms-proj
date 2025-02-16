from django.urls import path
from tasks.views import TaskView
from .views import CoursesListView, CourseDetailView, CreateRequest, FilteredCourses, CourseView


urlpatterns = [
    path('', CoursesListView.as_view(), name = "course-list"),
    path('course/id=<int:pk>/info', CourseDetailView.as_view(), name = "course-detail"),
    path('course/id=<int:pk>', CourseView.as_view(), name = "course"),
    path('course/id=<int:pk>/join', CreateRequest.as_view(), name = "create-request"),
    path('filter/<int:min_price>/<int:max_price>/', FilteredCourses.as_view(), name="filtered-list"),
    path('course/id=<int:pk>/task=<int:task_pk>', TaskView.as_view(), name = "task-detail"),
]