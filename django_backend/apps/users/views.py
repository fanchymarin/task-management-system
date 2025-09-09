from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'head']

    @action(methods=['get'], detail=False, url_path='me', url_name='me')
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

