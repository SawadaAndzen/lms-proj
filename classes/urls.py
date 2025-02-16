from django.urls import path
from .views import MyClassesListView, ClassDetailView, CreateClass, UpdateClass, DeleteClass


urlpatterns = [
    path('', MyClassesListView.as_view(), name = "groups-list"),
    path('group/?groupcode=<int:pk>', ClassDetailView.as_view(), name = "group-detail"),
    path('create/', CreateClass.as_view(), name = "create-group"),
    path('edit/<int:pk>/', UpdateClass.as_view(), name='edit-group'),
    path('delete/<int:pk>/', DeleteClass.as_view(), name='delete-group'),
]