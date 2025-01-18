from django.urls import path
from .views import MyClassesListView, ClassDetailView


urlpatterns = [
    path('', MyClassesListView.as_view(), name = "groups-list"),
    path('group/groupcode=<int:pk>', ClassDetailView.as_view(), name = "group-detail"),
]