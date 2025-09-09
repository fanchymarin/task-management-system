from rest_framework import serializers
from .models import Task, Tag, Comment


class AssignTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['assigned_to']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'created_at']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'title', 'status', 'priority', 'estimated_hours', 'actual_hours', 'created_by', 'assigned_to', 'parent_task']

class TaskDetailSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['url', 'title', 'description', 'status', 'priority', 'due_date', 'estimated_hours', 'actual_hours', 'created_by', 'assigned_to', 'parent_task', 'metadata', 'created_at', 'updated_at', 'is_archived', 'tags', 'comments']
