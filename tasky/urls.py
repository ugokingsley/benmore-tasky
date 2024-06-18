from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our task ViewSets with it.
router = DefaultRouter()
# router.register(r'tasks', TaskManagerViewSet, basename='tasks')
router.register("tasks", TaskManagerViewSet)
urlpatterns = router.urls
