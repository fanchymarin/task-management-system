from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'title', 'description', 'status', 'priority', 'due_date', 'estimated_hours', 'actual_hours', 'created_by', 'assigned_to', 'parent_task', 'metadata', 'created_at', 'updated_at', 'is_archived']
