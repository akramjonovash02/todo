from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import *
from .form import TaskForm

class TasksView(View):
    def get(self, request):
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user)
            context = {
                "tasks": tasks,
                "user": request.user
            }
            return render(request, 'index.html', context)
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('index')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class AddView(View):
    def get(self,request):
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = TaskForm()

        return render(request, 'index.html', {'form': form})

class EditView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('')
        else:
            form = TaskForm(instance=task)

        return render(request, 'edit.html', {'form': form})