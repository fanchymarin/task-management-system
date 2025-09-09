from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import AdminRenderer

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'head']
    pagination_class = UserPagination

    @action(methods=['get'], detail=False, url_path='me', url_name='me')
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

