from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('todos', views.todo_list, name='todo_list')
]