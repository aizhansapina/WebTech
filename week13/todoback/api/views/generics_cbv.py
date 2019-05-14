from rest_framework import generics
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from api.models import TaskList
from api.serializers import TaskListSerializer


class TaskListClass(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # return TaskList.objects.for_user(self.request.user)
        return TaskList.objects.all()
        # return TaskList.objects.filter(created_by__id=self.request.user)
    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer