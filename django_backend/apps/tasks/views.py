from rest_framework import viewsets
from .models import Task
from apps.users.models import User
from .serializers import TaskSerializer, TaskDetailSerializer, CommentSerializer, AssignTaskSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head']
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'assigned_to']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date']

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            return TaskDetailSerializer
        if self.action == 'manage_comments':
            return CommentSerializer
        if self.action == 'assign_task':
            return AssignTaskSerializer
        return TaskSerializer

    # Action to assign/unassign a user to/from a task

    @action(detail=True, methods=['get', 'post'], url_path='assign', url_name='assign')
    def assign_task(self, request, pk=None):
        task = self.get_object()
        
        if request.method == 'GET':
            # Return only the assigned_to field
            return Response({
                'assigned_to': TaskSerializer(task, context={'request': request}).data.get('assigned_to')
            })
        
        user_id = request.data.get('assigned_to')
        if not user_id:
            return Response({'Error': 'user_id is required'}, status=400)
        
        try:
            user = User.objects.get(id=user_id)
            if user in task.assigned_to.all():
                task.assigned_to.remove(user)
            else:
                task.assigned_to.add(user)
            task.save()
            return Response({'assigned_to': TaskSerializer(task, context={'request': request}).data.get('assigned_to')}, status=200)
        except User.DoesNotExist:
            return Response({'Error': 'User not found'}, status=404)
        
    # Action to view and add comments to a task
    @action(detail=True, methods=['get', 'post'], url_path='comments', url_name='comments', serializer_class=CommentSerializer)
    def manage_comments(self, request, pk=None):
        task = self.get_object()
        
        if request.method == 'GET':
            comments = CommentSerializer(task.comments.all(), many=True).data
            return Response(comments)
        
        serializer = CommentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        comment = serializer.save()
        task.comments.add(comment)
        task.save()

        comments = CommentSerializer(task.comments.all(), many=True).data
        return Response(comments, status=201)
