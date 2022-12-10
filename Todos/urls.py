from django.urls import path
from .views import TodoList,AddTodos,DeleteTodos

urlpatterns = [
  path('', TodoList, name='TodoList'),
  path('add_todo/', AddTodos, name='AddTodos'),
  path('delete_todo/<int:id>', DeleteTodos, name='DeleteTodos')
]