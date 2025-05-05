from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.

from .models import Task


def dashboard(request):
    return render(request, 'dashboard.html')

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Task.objects.create(title=title, description=description)
            return redirect('view_tasks')
    return render(request, 'add_task.html')


def view_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'view_tasks.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Update the task with the new data
        task.title = title
        task.description = description
        task.save()  # Save the updated task

        return redirect('view_tasks')  # Redirect to the task list page

    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('view_tasks')