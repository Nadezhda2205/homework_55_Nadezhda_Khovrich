from django.shortcuts import render
from tasks.models import Task

def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request=request, template_name='index.html', context=context)