from django.urls import path
from . import views

urlpatterns=[
    # path('',views.TodoView.as_view(),name='list'),
    path('items/<todo_list>',views.TodoItemListView.as_view()),
]