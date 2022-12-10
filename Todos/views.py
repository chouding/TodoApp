from django.shortcuts import render,redirect
from .models import Todo


def TodoList(request):
  context = { 'TodoList': Todo.objects.all()}
  return render(request, 'Todos/TodosList.html', context)

def AddTodos(request):
  todo = Todo(content = request.POST['content'])
  todo.save()
  return redirect('/')

def DeleteTodos(request, id):
  todo = Todo.objects.get(id=id)
  todo.delete()
  return redirect('/')