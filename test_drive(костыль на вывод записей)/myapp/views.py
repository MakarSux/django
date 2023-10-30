from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/general.html', {
        'name': 'Имя',
        'task': 'Комментарий',
        'phone_num': 'Номер телефона',
        'mail': 'Электронная почта',
        'name_car': 'Название машины'})

def about(request):
    return render(request, 'myapp/about.html')

def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'myapp/create.html', context)
