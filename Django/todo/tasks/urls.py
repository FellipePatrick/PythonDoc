from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloword),
    path('', views.taskList, name='task-list'),
]
