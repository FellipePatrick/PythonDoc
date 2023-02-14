from django.shortcuts import render
from django.http import HttpResponse


def helloword(request):
    return HttpResponse('Hello Word!')

def taskList(request):
    return render(request, 'index/index.html')

# Create your views here.
