from django.contrib import admin
from django.urls import path, include
from .views import tasklist_list, tasklist_detail, tasks_list, task_detail

urlpatterns = [
    path('task_list/', tasklist_list),
    path('task_list/<int:pk>', tasklist_detail),
    path('task_list/<int:pk>/tasks/', tasks_list),
    path('tasks/<int:pk>/', task_detail)
]