from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from django.core.handlers.wsgi import WSGIRequest
from tasks.services.config import CHOICES
import datetime
from tasks.forms import TaskForm


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'choices': CHOICES
    }
    return render(request=request, template_name='index.html', context=context)


def add_view(request:WSGIRequest):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if not form.is_valid():
            context = {
            'choices': CHOICES,
            'form': form
            }  
            return render(request=request, template_name='add.html', context=context)

        task: Task = Task.objects.create(**form.cleaned_data)
        return redirect('task_detail', pk=task.pk)
        
    form = TaskForm()
    context = {
        'choices': CHOICES,
        'form': form
    }    
    return render(request=request, template_name='add.html', context=context)


def edit_view(request: WSGIRequest, pk):
    task: Task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.header = request.POST.get('header')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.save()
        return redirect('task_detail', pk=pk)

    task.deadline = datetime.datetime.strftime(task.deadline, '%Y-%m-%d')
    context = {
        'task': task,
        'choices': CHOICES
    }
    return render(request=request, template_name='edit.html', context=context)


def delete_view(request, pk):
    Task.objects.filter(pk=pk).delete()
    return redirect('/')


def about_view(request):
    return render(request=request, template_name='about.html')


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task
    }
    return render(request, 'detail.html', context=context)
