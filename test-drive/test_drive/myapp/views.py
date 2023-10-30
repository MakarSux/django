from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def create(request):
    return render(request, 'myapp/create.html')
