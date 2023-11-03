from django.shortcuts import render
from tasks.models import Task  # Import the Task model

def combined_view(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = []

    return render(request, 'home.html', {'tasks': tasks})
