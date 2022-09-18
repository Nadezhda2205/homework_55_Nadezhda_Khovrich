from django.shortcuts import render, redirect
from tasks.models import Task
from django.core.handlers.wsgi import WSGIRequest

def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request=request, template_name='index.html', context=context)


def add_view(request:WSGIRequest):
    if request.method == 'POST':
        return redirect('/')
    return render(request=request, template_name='add.html')