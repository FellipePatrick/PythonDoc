from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from .models import Task

def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'index/index.html', {'tasks':tasks})

def taskView(request, id):
    tasks = get_list_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'tasks':tasks} )

# Create your views here.
