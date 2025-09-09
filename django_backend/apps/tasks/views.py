from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
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
        if self.action == 'retrieve':
            return TaskDetailSerializer
        return TaskSerializer

    @action(detail=True, methods=['get', 'post'], url_path='assign', url_name='assign')
    def assign_task(self, request, pk=None):
        task = self.get_object()
        
        if request.method == 'GET':
            serializer = self.get_serializer(task)
            return Response(serializer.data)
        
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'user_id is required'}, status=400)
        
        from apps.users.models import User
        try:
            user = User.objects.get(id=user_id)
            if user in task.assigned_to.all():
                task.assigned_to.remove(user)
            else:
                task.assigned_to.add(user)
            task.save()
            serializer = self.get_serializer(task)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
