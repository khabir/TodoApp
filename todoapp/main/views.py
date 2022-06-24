from django.shortcuts import render

from .models import Todo

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def  todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todolist.html', {'todos': todos})
