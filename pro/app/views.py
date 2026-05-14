

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

def home(request):

    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(title=task)

        return redirect('/')

    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search)
    else:
        tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }

    return render(request, 'home.html', context)
def delete_task(request, id):

    task = Task.objects.get(id=id)

    task.delete()

    return redirect('/')
def update_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == "POST":

        new_task = request.POST.get('task')

        task.title = new_task

        task.save()

        return redirect('/')

    context = {
        'task': task
    }

    return render(request, 'update.html', context)
def complete_task(request, id):

    task = Task.objects.get(id=id)

    task.completed = not task.completed

    task.save()

    return redirect('/')