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
        task_data = {
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'deadline': request.POST.get('deadline')
        }

        Task.objects.create(**task_data)
        return redirect('/')
    return render(request=request, template_name='add.html')

def edit_view(request):
    return render(request=request, template_name='edit.html')
