from django.shortcuts import render
from .models import Task, TaskList
from django.http import JsonResponse
# Create your views here.

def tasklist_list(request):
    if request.method == 'GET':
        list_of_tasklists = TaskList.objects.all()
        json_task_lists = [t.to_json() for t in list_of_tasklists]
    return JsonResponse(json_task_lists, safe=False)

def tasklist_detail(request, pk):
    try:
        tasklists = TaskList.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)
    return JsonResponse(tasklists.to_json())

def tasks_list(request, pk):
    if request.method == 'GET':
        try:
            task_list = TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        tasks = task_list.task_set.all()
        json_tasks = [t.to_json() for t in tasks]

    return JsonResponse(json_tasks, safe=False)

def task_detail(request, pk):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_task = task.to_json_all()
        return JsonResponse(json_task)
