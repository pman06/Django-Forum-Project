from django.shortcuts import render, redirect
from .models import TaskDb
from .forms import TaskForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_tasks = TaskDb.objects.all()
            messages.success(request, ("Task Added Successfully"))
            return render(request, 'index.html', context ={'objects':all_tasks})
    else:
        all_tasks = TaskDb.objects.all()
        form = TaskForm();
        return render(request, 'index.html', context ={'objects':all_tasks, 'form':form})

def delete(request, list_id):
    item = TaskDb.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Deleted'))
    return redirect('home')
