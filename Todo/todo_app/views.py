from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from .models import TodoItem,TodoList

# Create your views here.

# class TodoView(ListView):
#     model = TodoList
#     template_name = "todo/todo_list.html"
    
class TodoItemListView(ListView):
    # model = TodoItem
    template_name = "todo/todo_items.html"
    
    def get_queryset(self):
        self.todo_list = get_object_or_404(TodoList, title=self.kwargs['todo_list'])
        return TodoItem.objects.filter(todo_list = self.todo_list)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['todo_list'] = self.todo_list
        return context