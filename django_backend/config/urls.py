"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from .views import health_check
from apps.users.views import UserViewSet
from apps.tasks.views import TaskViewSet
from apps.common.views import home_view
from django.views.generic import RedirectView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
	# Authorization views
	path('', home_view, name='home'),
	path('accounts/profile/', RedirectView.as_view(url='/api/', permanent=False)),
	
    # API views
    path('api/', include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
	
    # Health check endpoint
    path('health/', health_check, name='health_check')
]
