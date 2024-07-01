from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .permissions import *

from .models import CustomUser, Task
from .serializers import UserInfo, TaskSerializer


class UserView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfo
    permission_classes = (IsAuthenticated,)


class UserCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfo
    permission_classes = (IsEmployee, IsAuthenticated,)


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAssignedToTask, CanViewTask, IsAuthenticated,)


class TaskCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsCustomer, IsAuthenticated,)

    def perform_assign(self, serializer):
        task = self.get_object()
        if task.status == 'PENDING' and task.assigned_to == self.request.user:
            task.status = 'IN_PROGRESS'
            serializer.save()


class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (CanEditTask, IsAuthenticated,)
