from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
]