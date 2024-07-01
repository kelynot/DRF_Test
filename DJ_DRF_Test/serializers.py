from rest_framework import serializers
from .models import CustomUser, Task


class UserInfo(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'



