from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks':tasks})

def taskView(request, id):
    tasks = get_list_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'tasks':tasks} )

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/') 
    
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form':form})



def editTask(request, id):
    task = get_list_or_404(Task, pk=id)
    form = TaskForm()
    for i in task:
        title = i.title

    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/') 
        else: 
            return render(request, 'tasks/edittask.html', {'form':form, 'title':title})
    else:
        return render(request, 'tasks/edittask.html', {'form':form, 'title':title})